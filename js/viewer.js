import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { on, getPartById, getState } from './store.js';

let scene, camera, renderer, controls;
let droneGroup;
const partMeshes = {};

// Attachment positions relative to drone center (in scene units; 1 unit ≈ 10mm)
const ATTACH = {
  frame:     new THREE.Vector3(0, 0, 0),
  motor_fl:  new THREE.Vector3(-10, 0, -10),
  motor_fr:  new THREE.Vector3( 10, 0, -10),
  motor_rl:  new THREE.Vector3(-10, 0,  10),
  motor_rr:  new THREE.Vector3( 10, 0,  10),
  esc:       new THREE.Vector3(0,  0.5, 0),
  fc:        new THREE.Vector3(0,  1.5, 0),
  camera:    new THREE.Vector3(0,  1.8, -11),
  vtx:       new THREE.Vector3(0,  1.2,  8),
  battery:   new THREE.Vector3(0, -2.5, 1),
  receiver:  new THREE.Vector3(-3, 0.5, 5),
  prop_fl:   new THREE.Vector3(-10, 1.2, -10),
  prop_fr:   new THREE.Vector3( 10, 1.2, -10),
  prop_rl:   new THREE.Vector3(-10, 1.2,  10),
  prop_rr:   new THREE.Vector3( 10, 1.2,  10),
};

export function init() {
  const canvas = document.getElementById('drone-canvas');
  const parent = canvas.parentElement;

  // Renderer
  renderer = new THREE.WebGLRenderer({ canvas, antialias: true, alpha: false });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type = THREE.PCFSoftShadowMap;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.1;
  resize();

  // Scene
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x08080f);
  scene.fog = new THREE.FogExp2(0x08080f, 0.018);

  // Camera
  camera = new THREE.PerspectiveCamera(50, canvas.width / canvas.height, 0.1, 500);
  camera.position.set(30, 22, 35);
  camera.lookAt(0, 0, 0);

  // Controls
  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.minDistance = 8;
  controls.maxDistance = 80;
  controls.maxPolarAngle = Math.PI * 0.85;
  controls.target.set(0, 0, 0);

  // Lighting
  const ambient = new THREE.AmbientLight(0x334466, 1.2);
  scene.add(ambient);

  const key = new THREE.DirectionalLight(0xffffff, 2.5);
  key.position.set(20, 40, 20);
  key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048);
  key.shadow.camera.near = 1;
  key.shadow.camera.far = 120;
  key.shadow.camera.left = key.shadow.camera.bottom = -30;
  key.shadow.camera.right = key.shadow.camera.top = 30;
  scene.add(key);

  const fill = new THREE.DirectionalLight(0x4488ff, 0.8);
  fill.position.set(-20, 10, -15);
  scene.add(fill);

  const rim = new THREE.DirectionalLight(0x00c8ff, 0.6);
  rim.position.set(0, -10, 20);
  scene.add(rim);

  // Ground grid
  const grid = new THREE.GridHelper(80, 40, 0x1a1a2e, 0x141428);
  grid.position.y = -6;
  scene.add(grid);

  // Ground shadow catcher
  const groundGeo = new THREE.PlaneGeometry(80, 80);
  const groundMat = new THREE.ShadowMaterial({ opacity: 0.4 });
  const ground = new THREE.Mesh(groundGeo, groundMat);
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -6;
  ground.receiveShadow = true;
  scene.add(ground);

  // Drone group
  droneGroup = new THREE.Group();
  scene.add(droneGroup);

  // Subtle idle animation
  let t = 0;
  const idleFloat = () => {
    t += 0.008;
    droneGroup.position.y = Math.sin(t) * 0.3;
    droneGroup.rotation.y = Math.sin(t * 0.4) * 0.04;
  };

  // Render loop
  (function animate() {
    requestAnimationFrame(animate);
    idleFloat();
    controls.update();
    renderer.render(scene, camera);
  })();

  // Resize
  window.addEventListener('resize', resize);

  // Store events
  on('build:changed', ({ build }) => syncBuildToViewer(build));

  // Reset camera button
  document.getElementById('btn-reset-camera').addEventListener('click', resetCamera);

  // Screenshot
  document.getElementById('btn-screenshot').addEventListener('click', screenshot);
}

function syncBuildToViewer(build) {
  const { catalog } = getState();

  clearAllParts();

  const frame = getPartById(build['frame']);
  const frameScale = frame ? frameScaleFactor(frame) : 1;

  if (build['frame']) addFrameMesh(getPartById(build['frame']), frameScale);
  if (build['motor']) addMotorMeshes(getPartById(build['motor']), frameScale);
  if (build['esc'])   addESCMesh(getPartById(build['esc']));
  if (build['fc'])    addFCMesh(getPartById(build['fc']));
  if (build['propeller']) addPropMeshes(getPartById(build['propeller']), frameScale);
  if (build['camera'])    addCameraMesh(getPartById(build['camera']), frameScale);
  if (build['vtx'])       addVTXMesh(getPartById(build['vtx']));
  if (build['battery'])   addBatteryMesh(getPartById(build['battery']));
  if (build['receiver'])  addReceiverMesh(getPartById(build['receiver']));

  updateHint(build);
}

function clearAllParts() {
  Object.values(partMeshes).forEach(mesh => {
    if (mesh) droneGroup.remove(mesh);
  });
  Object.keys(partMeshes).forEach(k => delete partMeshes[k]);
}

function frameScaleFactor(part) {
  const size = part.specs.size_mm || 215;
  return size / 215;
}

function mat(color, opts = {}) {
  return new THREE.MeshStandardMaterial({
    color: new THREE.Color(color),
    roughness: opts.roughness ?? 0.55,
    metalness: opts.metalness ?? 0.3,
    ...(opts.emissive ? { emissive: new THREE.Color(opts.emissive), emissiveIntensity: opts.emissiveIntensity ?? 0.15 } : {}),
  });
}

function addAndAnimate(key, mesh) {
  mesh.scale.set(0.01, 0.01, 0.01);
  droneGroup.add(mesh);
  partMeshes[key] = mesh;

  // pop-in animation
  const start = performance.now();
  const dur = 350;
  function grow() {
    const t = Math.min((performance.now() - start) / dur, 1);
    const ease = 1 - Math.pow(1 - t, 3);
    mesh.scale.setScalar(ease);
    if (t < 1) requestAnimationFrame(grow);
  }
  requestAnimationFrame(grow);
}

// ── FRAME ─────────────────────────────────────────────

function addFrameMesh(part, scale) {
  const color = part.color || '#1a1a1a';
  const g = new THREE.Group();

  // Center plate
  const centerGeo = new THREE.BoxGeometry(6 * scale, 0.8, 5 * scale);
  const centerMesh = new THREE.Mesh(centerGeo, mat(color, { roughness: 0.3, metalness: 0.7 }));
  centerMesh.castShadow = true;
  g.add(centerMesh);

  // 4 arms (X pattern)
  const armDirs = [
    [-1, -1], [1, -1], [-1, 1], [1, 1]
  ];
  const armLen = 11 * scale;
  armDirs.forEach(([dx, dz]) => {
    const armGeo = new THREE.BoxGeometry(armLen, 0.5, 1.4 * scale);
    const armMesh = new THREE.Mesh(armGeo, mat(color, { roughness: 0.25, metalness: 0.8 }));
    armMesh.position.set(dx * armLen * 0.42, 0, dz * armLen * 0.42);
    armMesh.rotation.y = Math.atan2(dz, dx);
    armMesh.castShadow = true;
    g.add(armMesh);
  });

  // Top plate
  const topGeo = new THREE.BoxGeometry(5 * scale, 0.4, 4 * scale);
  const topMesh = new THREE.Mesh(topGeo, mat(color, { roughness: 0.2, metalness: 0.85 }));
  topMesh.position.y = 1.2;
  g.add(topMesh);

  addAndAnimate('frame', g);
}

// ── MOTORS ────────────────────────────────────────────

function addMotorMeshes(part, scale) {
  const color = part.color || '#2a2a2a';
  const positions = [ATTACH.motor_fl, ATTACH.motor_fr, ATTACH.motor_rl, ATTACH.motor_rr];
  const motorGroup = new THREE.Group();

  positions.forEach(pos => {
    const m = makeMotorMesh(color, scale);
    m.position.copy(pos);
    motorGroup.add(m);
  });

  addAndAnimate('motor', motorGroup);
}

function makeMotorMesh(color, scale) {
  const g = new THREE.Group();

  // Motor can (bell)
  const bellGeo = new THREE.CylinderGeometry(1.2 * scale, 1.3 * scale, 1.8 * scale, 16);
  const bell = new THREE.Mesh(bellGeo, mat(color, { roughness: 0.2, metalness: 0.9 }));
  bell.position.y = 0.9;
  bell.castShadow = true;
  g.add(bell);

  // Stator base
  const baseGeo = new THREE.CylinderGeometry(1.3 * scale, 1.3 * scale, 0.5, 16);
  const base = new THREE.Mesh(baseGeo, mat('#111', { roughness: 0.5, metalness: 0.4 }));
  base.castShadow = true;
  g.add(base);

  // Shaft
  const shaftGeo = new THREE.CylinderGeometry(0.25, 0.25, 2.5 * scale, 8);
  const shaft = new THREE.Mesh(shaftGeo, mat('#888', { roughness: 0.1, metalness: 1 }));
  shaft.position.y = 1.5;
  g.add(shaft);

  // Motor screws (visual detail)
  [0, 90, 180, 270].forEach(angle => {
    const screwGeo = new THREE.CylinderGeometry(0.08, 0.08, 0.3, 6);
    const screw = new THREE.Mesh(screwGeo, mat('#555', { metalness: 1, roughness: 0.1 }));
    const rad = THREE.MathUtils.degToRad(angle);
    screw.position.set(Math.cos(rad) * 1.0 * scale, 0.25, Math.sin(rad) * 1.0 * scale);
    g.add(screw);
  });

  return g;
}

// ── PROPS ─────────────────────────────────────────────

function addPropMeshes(part, scale) {
  const diameter = (part.specs.diameter_inch || 5) * 1.27; // inch → cm → units
  const blades   = part.specs.blade_count || 3;
  const positions = [ATTACH.prop_fl, ATTACH.prop_fr, ATTACH.prop_rl, ATTACH.prop_rr];
  const propGroup = new THREE.Group();
  const propScale = diameter / 12.7;

  positions.forEach((pos, i) => {
    const p = makePropMesh(blades, propScale);
    p.position.copy(pos);
    p.rotation.y = (i % 2 === 0 ? 1 : -1) * 0.4; // slight alternating angle
    propGroup.add(p);
  });

  addAndAnimate('propeller', propGroup);
}

function makePropMesh(blades, scale) {
  const g = new THREE.Group();
  const propMat = mat('#111111', { roughness: 0.6, metalness: 0.1 });

  for (let i = 0; i < blades; i++) {
    const bladeGeo = new THREE.BoxGeometry(5 * scale, 0.12, 1.1 * scale);
    const blade = new THREE.Mesh(bladeGeo, propMat);
    blade.rotation.y = (i / blades) * Math.PI * 2;
    blade.rotation.z = 0.08; // pitch angle
    blade.position.set(
      Math.cos((i / blades) * Math.PI * 2) * 2.5 * scale,
      0,
      Math.sin((i / blades) * Math.PI * 2) * 2.5 * scale
    );
    blade.castShadow = true;
    g.add(blade);
  }

  // Hub
  const hubGeo = new THREE.CylinderGeometry(0.35, 0.35, 0.3, 8);
  g.add(new THREE.Mesh(hubGeo, mat('#333', { metalness: 0.8, roughness: 0.2 })));

  return g;
}

// ── ESC ───────────────────────────────────────────────

function addESCMesh(part) {
  const size = part.specs.form_factor_mm === 20 ? 2.5 : 3.8;
  const g = new THREE.Group();

  const boardGeo = new THREE.BoxGeometry(size * 2, 0.25, size * 2);
  const board = new THREE.Mesh(boardGeo, mat('#003300', { roughness: 0.8, metalness: 0.1 }));
  board.castShadow = true;
  g.add(board);

  // MOSFETs (corners)
  [[-size*0.6, -size*0.6],[size*0.6,-size*0.6],[-size*0.6,size*0.6],[size*0.6,size*0.6]].forEach(([x,z]) => {
    const mosfetGeo = new THREE.BoxGeometry(0.9, 0.4, 0.65);
    const mosfet = new THREE.Mesh(mosfetGeo, mat('#111', { roughness: 0.4, metalness: 0.6 }));
    mosfet.position.set(x, 0.32, z);
    g.add(mosfet);
  });

  g.position.copy(ATTACH.esc);
  addAndAnimate('esc', g);
}

// ── FC ────────────────────────────────────────────────

function addFCMesh(part) {
  const size = part.specs.form_factor_mm === 20 ? 2.2 : 3.4;
  const g = new THREE.Group();

  const boardGeo = new THREE.BoxGeometry(size * 2, 0.2, size * 2);
  const board = new THREE.Mesh(boardGeo, mat('#000044', { roughness: 0.7, metalness: 0.15 }));
  board.castShadow = true;
  g.add(board);

  // Gyro chip
  const chipGeo = new THREE.BoxGeometry(0.8, 0.15, 0.8);
  const chip = new THREE.Mesh(chipGeo, mat('#222244', { roughness: 0.3, metalness: 0.5 }));
  chip.position.y = 0.17;
  g.add(chip);

  // LED glow hint
  const ledGeo = new THREE.BoxGeometry(0.2, 0.1, 0.2);
  const ledMat = new THREE.MeshStandardMaterial({ color: 0x00c8ff, emissive: 0x00c8ff, emissiveIntensity: 2 });
  const led = new THREE.Mesh(ledGeo, ledMat);
  led.position.set(size * 0.7, 0.2, size * 0.7);
  g.add(led);

  g.position.copy(ATTACH.fc);
  addAndAnimate('fc', g);
}

// ── CAMERA ────────────────────────────────────────────

function addCameraMesh(part, scale) {
  const g = new THREE.Group();

  // Camera body
  const bodyGeo = new THREE.BoxGeometry(1.4, 1.4, 1.8);
  const body = new THREE.Mesh(bodyGeo, mat('#111', { roughness: 0.5, metalness: 0.5 }));
  body.castShadow = true;
  g.add(body);

  // Lens
  const lensGeo = new THREE.CylinderGeometry(0.45, 0.45, 0.4, 16);
  lensGeo.rotateX(Math.PI / 2);
  const lens = new THREE.Mesh(lensGeo, mat('#001133', { roughness: 0.05, metalness: 0.8 }));
  lens.position.z = -1.1;
  g.add(lens);

  // Lens glass
  const glassGeo = new THREE.CircleGeometry(0.38, 16);
  const glassMat = new THREE.MeshStandardMaterial({
    color: 0x002244,
    roughness: 0,
    metalness: 0.1,
    transparent: true,
    opacity: 0.7,
  });
  const glass = new THREE.Mesh(glassGeo, glassMat);
  glass.rotation.y = Math.PI;
  glass.position.z = -1.31;
  g.add(glass);

  const pos = ATTACH.camera.clone().multiplyScalar(scale);
  pos.y = ATTACH.camera.y;
  g.position.copy(pos);
  g.rotation.x = 0.35;
  addAndAnimate('camera', g);
}

// ── VTX ───────────────────────────────────────────────

function addVTXMesh(part) {
  const g = new THREE.Group();

  const boardGeo = new THREE.BoxGeometry(2.4, 0.3, 2.4);
  g.add(new THREE.Mesh(boardGeo, mat('#221100', { roughness: 0.7, metalness: 0.2 })));

  // Antenna
  const antGeo = new THREE.CylinderGeometry(0.08, 0.08, 4, 6);
  const ant = new THREE.Mesh(antGeo, mat('#888', { roughness: 0.2, metalness: 0.9 }));
  ant.position.set(0.8, 2.2, 0);
  ant.rotation.z = 0.2;
  g.add(ant);

  // LED
  const ledMat = new THREE.MeshStandardMaterial({ color: 0xff4400, emissive: 0xff4400, emissiveIntensity: 1.5 });
  const led = new THREE.Mesh(new THREE.BoxGeometry(0.18, 0.12, 0.18), ledMat);
  led.position.set(-0.8, 0.22, 0.8);
  g.add(led);

  g.position.copy(ATTACH.vtx);
  addAndAnimate('vtx', g);
}

// ── BATTERY ───────────────────────────────────────────

function addBatteryMesh(part) {
  const cellCount = part.specs.cell_count_s || 4;
  const capacity  = part.specs.capacity_mah || 1500;
  const len = 10 + (capacity - 850) / 500;
  const w   = 3.2 + cellCount * 0.4;
  const h   = 2.2 + cellCount * 0.2;

  const g = new THREE.Group();

  const bodyGeo = new THREE.BoxGeometry(w, h, Math.min(len, 14));
  g.add(new THREE.Mesh(bodyGeo, mat(part.color || '#1a0000', { roughness: 0.7, metalness: 0.05 })));

  // XT60 connector
  const connGeo = new THREE.BoxGeometry(1.2, 0.9, 0.7);
  const conn = new THREE.Mesh(connGeo, mat('#cc8800', { roughness: 0.3, metalness: 0.8 }));
  conn.position.z = -len / 2 - 0.35;
  g.add(conn);

  // Cell separators
  for (let i = 1; i < cellCount; i++) {
    const sepGeo = new THREE.BoxGeometry(w + 0.1, h + 0.1, 0.08);
    const sep = new THREE.Mesh(sepGeo, mat('#000', { roughness: 1, metalness: 0 }));
    sep.position.z = -len / 2 + (len / cellCount) * i;
    g.add(sep);
  }

  g.position.copy(ATTACH.battery);
  addAndAnimate('battery', g);
}

// ── RECEIVER ─────────────────────────────────────────

function addReceiverMesh(part) {
  const g = new THREE.Group();

  const boardGeo = new THREE.BoxGeometry(1.6, 0.2, 1.2);
  g.add(new THREE.Mesh(boardGeo, mat('#1a001a', { roughness: 0.8, metalness: 0.1 })));

  // Antenna wires
  const antennaPositions = part.specs.frequency_mhz >= 2000
    ? [[-0.5, 0], [0.5, 0]]
    : [[-0.5, 0]];

  antennaPositions.forEach(([x]) => {
    const antGeo = new THREE.CylinderGeometry(0.04, 0.04, 3.5, 4);
    const ant = new THREE.Mesh(antGeo, mat('#ff8800', { roughness: 0.4, metalness: 0.1 }));
    ant.position.set(x, 1.95, 0);
    ant.rotation.z = x > 0 ? 0.3 : -0.3;
    g.add(ant);
  });

  g.position.copy(ATTACH.receiver);
  addAndAnimate('receiver', g);
}

// ── HELPERS ───────────────────────────────────────────

function updateHint(build) {
  const count  = Object.keys(build).length;
  const hint   = document.getElementById('hud-hint');
  const total  = 9;
  if (count === 0) {
    hint.textContent = 'Select a component to begin building';
    hint.classList.remove('hidden');
  } else if (count === total) {
    hint.textContent = 'Build complete! ';
    setTimeout(() => hint.classList.add('hidden'), 3000);
  } else {
    hint.textContent = `${count}/${total} components selected`;
    hint.classList.remove('hidden');
  }
}

function resize() {
  const parent = renderer.domElement.parentElement;
  const w = parent.clientWidth;
  const h = parent.clientHeight;
  renderer.setSize(w, h);
  if (camera) {
    camera.aspect = w / h;
    camera.updateProjectionMatrix();
  }
}

function resetCamera() {
  controls.reset();
  camera.position.set(30, 22, 35);
  camera.lookAt(0, 0, 0);
  controls.target.set(0, 0, 0);
}

function screenshot() {
  renderer.render(scene, camera);
  const link = document.createElement('a');
  link.download = 'fpv-build.png';
  link.href = renderer.domElement.toDataURL('image/png');
  link.click();
}
