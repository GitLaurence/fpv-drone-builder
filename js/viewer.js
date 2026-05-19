import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { on, getState, getPartById } from './store.js';

let scene, camera, renderer, controls;
let droneGroup;
const partMeshes = {};

const ATTACH = {
  frame:    new THREE.Vector3(0,    0,    0),
  motor:    null, // handled as 4-point group
  motor_fl: new THREE.Vector3(-10,  0.3, -10),
  motor_fr: new THREE.Vector3( 10,  0.3, -10),
  motor_rl: new THREE.Vector3(-10,  0.3,  10),
  motor_rr: new THREE.Vector3( 10,  0.3,  10),
  esc:      new THREE.Vector3(0,    0.6,   0),
  fc:       new THREE.Vector3(0,    1.8,   0),
  camera:   new THREE.Vector3(0,    2.2, -11),
  vtx:      new THREE.Vector3(0,    1.4,   8),
  battery:  new THREE.Vector3(0,   -2.8,   1),
  receiver: new THREE.Vector3(-3,   0.8,   5),
  prop_fl:  new THREE.Vector3(-10,  1.6, -10),
  prop_fr:  new THREE.Vector3( 10,  1.6, -10),
  prop_rl:  new THREE.Vector3(-10,  1.6,  10),
  prop_rr:  new THREE.Vector3( 10,  1.6,  10),
};

const SLOT_CAM = {
  frame:     { pos: new THREE.Vector3(26, 20, 30),   look: new THREE.Vector3(0,   0,   0) },
  motor:     { pos: new THREE.Vector3(20, 14, 22),   look: new THREE.Vector3(10,  0,  10) },
  esc:       { pos: new THREE.Vector3(8,  14, 16),   look: new THREE.Vector3(0,   0.6, 0) },
  fc:        { pos: new THREE.Vector3(8,  15, 16),   look: new THREE.Vector3(0,   1.8, 0) },
  propeller: { pos: new THREE.Vector3(16, 22, 18),   look: new THREE.Vector3(8,   1.6, 8) },
  camera:    { pos: new THREE.Vector3(0,  12, -22),  look: new THREE.Vector3(0,   2.2,-11) },
  vtx:       { pos: new THREE.Vector3(10, 12,  22),  look: new THREE.Vector3(0,   1.4, 8) },
  battery:   { pos: new THREE.Vector3(10,  2,  20),  look: new THREE.Vector3(0,  -2.8, 1) },
  receiver:  { pos: new THREE.Vector3(-16, 10, 18),  look: new THREE.Vector3(-3,  0.8, 5) },
};
const DEFAULT_CAM = {
  pos:  new THREE.Vector3(30, 22, 35),
  look: new THREE.Vector3(0, 0, 0),
};

let camAnim    = null;
let activeSlot = null;
let _renderer  = null; // exposed for export.js

export function getRenderer() { return _renderer; }

export function init() {
  const canvas = document.getElementById('drone-canvas');

  renderer = new THREE.WebGLRenderer({
    canvas,
    antialias: true,
    preserveDrawingBuffer: true,
  });
  _renderer = renderer;
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.shadowMap.type    = THREE.PCFSoftShadowMap;
  renderer.toneMapping       = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.15;
  resize();

  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x08080f);
  scene.fog = new THREE.FogExp2(0x08080f, 0.015);

  camera = new THREE.PerspectiveCamera(50, 1, 0.1, 500);
  camera.position.copy(DEFAULT_CAM.pos);

  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;
  controls.dampingFactor = 0.06;
  controls.minDistance = 8;
  controls.maxDistance = 90;
  controls.maxPolarAngle = Math.PI * 0.86;
  controls.target.copy(DEFAULT_CAM.look);

  // Cancel camera animation on user drag
  renderer.domElement.addEventListener('pointerdown', () => { camAnim = null; });

  // Lighting
  scene.add(new THREE.AmbientLight(0x2233aa, 1.4));

  const key = new THREE.DirectionalLight(0xffffff, 2.8);
  key.position.set(20, 40, 20);
  key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048);
  Object.assign(key.shadow.camera, { near: 1, far: 120, left: -32, right: 32, top: 32, bottom: -32 });
  scene.add(key);

  const fill = new THREE.DirectionalLight(0x4488ff, 0.9);
  fill.position.set(-20, 8, -15);
  scene.add(fill);

  const rim = new THREE.DirectionalLight(0x00c8ff, 0.7);
  rim.position.set(0, -8, 20);
  scene.add(rim);

  // Grid
  const grid = new THREE.GridHelper(80, 40, 0x161630, 0x111128);
  grid.position.y = -6;
  scene.add(grid);

  // Shadow catcher
  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(80, 80),
    new THREE.ShadowMaterial({ opacity: 0.45 })
  );
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -6;
  ground.receiveShadow = true;
  scene.add(ground);

  droneGroup = new THREE.Group();
  scene.add(droneGroup);

  // Expose for export.js (not official Three.js API, just a tag)
  renderer._scene  = scene;
  renderer._camera = camera;

  let t = 0;
  const idle = () => {
    t += 0.007;
    droneGroup.position.y  = Math.sin(t) * 0.28;
    droneGroup.rotation.y  = Math.sin(t * 0.35) * 0.035;
  };

  (function loop() {
    requestAnimationFrame(loop);

    // Camera lerp
    if (camAnim) {
      const raw  = Math.min((performance.now() - camAnim.start) / camAnim.dur, 1);
      const ease = 1 - Math.pow(1 - raw, 3);
      camera.position.lerpVectors(camAnim.fromPos, camAnim.toPos, ease);
      controls.target.lerpVectors(camAnim.fromLook, camAnim.toLook, ease);
      if (raw >= 1) camAnim = null;
    }

    // Prop spin when motor selected
    const { build } = getState();
    if (partMeshes.propeller && build.motor) {
      partMeshes.propeller.children.forEach((pg, i) => {
        pg.rotation.y += i % 2 === 0 ? 0.22 : -0.22;
      });
    }

    idle();
    controls.update();
    renderer.render(scene, camera);
  })();

  window.addEventListener('resize', resize);

  on('build:changed', ({ build }) => syncBuild(build));
  on('slot:active',   ({ slot }) => {
    activeSlot = slot;
    highlightSlot(slot);
    if (slot) startCamAnim(SLOT_CAM[slot]);
    else      startCamAnim(DEFAULT_CAM);
  });

  document.getElementById('btn-reset-camera').addEventListener('click', resetCamera);
  document.getElementById('btn-screenshot').addEventListener('click', screenshot);
}

// ── Camera animation ─────────────────────────────────

function startCamAnim(target) {
  if (!target) return;
  camAnim = {
    fromPos:  camera.position.clone(),
    fromLook: controls.target.clone(),
    toPos:    target.pos.clone(),
    toLook:   target.look.clone(),
    start:    performance.now(),
    dur:      650,
  };
}

// ── Slot highlighting ────────────────────────────────

function highlightSlot(slotKey) {
  // Reset all
  Object.values(partMeshes).forEach(mesh => {
    if (!mesh) return;
    mesh.traverse(child => {
      if (!child.isMesh || !child.material) return;
      const ud = child.material.userData;
      child.material.emissive.set(ud.origEmissive || 0);
      child.material.emissiveIntensity = ud.origEmissiveIntensity ?? 0;
    });
  });

  const target = partMeshes[slotKey];
  if (!slotKey || !target) return;

  target.traverse(child => {
    if (!child.isMesh || !child.material) return;
    child.material.emissive.setHex(0x00c8ff);
    child.material.emissiveIntensity = 0.45;
  });
}

// ── Build sync ───────────────────────────────────────

function syncBuild(build) {
  clearAll();

  const frame      = getPartById(build.frame);
  const frameScale = frame ? frame.specs.size_mm / 215 : 1;

  if (build.frame)     addFrameMesh(frame, frameScale);
  if (build.motor)     addMotorMeshes(getPartById(build.motor), frameScale);
  if (build.esc)       addESCMesh(getPartById(build.esc));
  if (build.fc)        addFCMesh(getPartById(build.fc));
  if (build.propeller) addPropMeshes(getPartById(build.propeller), frameScale);
  if (build.camera)    addCameraMesh(getPartById(build.camera), frameScale);
  if (build.vtx)       addVTXMesh(getPartById(build.vtx));
  if (build.battery)   addBatteryMesh(getPartById(build.battery));
  if (build.receiver)  addReceiverMesh(getPartById(build.receiver));

  // Re-apply highlight if a slot is active
  if (activeSlot) highlightSlot(activeSlot);

  updateHint(build);
}

function clearAll() {
  Object.values(partMeshes).forEach(m => { if (m) droneGroup.remove(m); });
  Object.keys(partMeshes).forEach(k => delete partMeshes[k]);
}

// ── Material helper ──────────────────────────────────

function mat(hex, { roughness = 0.55, metalness = 0.3, emissive, emissiveIntensity = 0.15 } = {}) {
  const m = new THREE.MeshStandardMaterial({
    color:    new THREE.Color(hex),
    roughness,
    metalness,
  });
  if (emissive) {
    m.emissive.setHex(emissive);
    m.emissiveIntensity = emissiveIntensity;
    m.userData.origEmissive = emissive;
    m.userData.origEmissiveIntensity = emissiveIntensity;
  } else {
    m.userData.origEmissive = 0;
    m.userData.origEmissiveIntensity = 0;
  }
  return m;
}

// ── Pop-in animation ─────────────────────────────────

function popIn(mesh) {
  mesh.scale.setScalar(0.01);
  droneGroup.add(mesh);
  const start = performance.now(), dur = 380;
  const tick = () => {
    const t    = Math.min((performance.now() - start) / dur, 1);
    const ease = 1 - Math.pow(1 - t, 3);
    mesh.scale.setScalar(ease);
    if (t < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}

function add(key, mesh) {
  partMeshes[key] = mesh;
  popIn(mesh);
}

// ── FRAME ────────────────────────────────────────────

function addFrameMesh(part, scale) {
  const color = part.color || '#1a1a1a';
  const g = new THREE.Group();
  const cfrMat = mat(color, { roughness: 0.22, metalness: 0.82 });

  // Center plate
  g.add(boxAt(cfrMat, 6 * scale, 0.7, 4.5 * scale, 0, 0, 0, true));

  // Top plate
  g.add(boxAt(mat(color, { roughness: 0.18, metalness: 0.88 }), 4.5 * scale, 0.4, 3.5 * scale, 0, 1.1, 0));

  // 4 arms in X pattern
  const armLen = 11 * scale;
  [[-1,-1],[1,-1],[-1,1],[1,1]].forEach(([dx, dz]) => {
    const arm = boxAt(cfrMat, armLen, 0.45, 1.3 * scale, dx * armLen * 0.43, 0, dz * armLen * 0.43, true);
    arm.rotation.y = Math.atan2(dz, dx);
    g.add(arm);
  });

  // Standoffs (4 vertical cylinders connecting plates)
  [-1,1].forEach(sx => [-1,1].forEach(sz => {
    const cyl = new THREE.Mesh(
      new THREE.CylinderGeometry(0.18, 0.18, 1.15, 6),
      mat('#333', { roughness: 0.3, metalness: 0.9 })
    );
    cyl.position.set(sx * 1.8 * scale, 0.55, sz * 1.4 * scale);
    g.add(cyl);
  }));

  // Motor-mount circles at arm ends
  [ATTACH.motor_fl, ATTACH.motor_fr, ATTACH.motor_rl, ATTACH.motor_rr].forEach(pos => {
    const ring = new THREE.Mesh(
      new THREE.TorusGeometry(1.35 * scale, 0.12, 6, 16),
      mat('#444', { roughness: 0.2, metalness: 0.95 })
    );
    ring.rotation.x = Math.PI / 2;
    ring.position.copy(pos);
    g.add(ring);
  });

  add('frame', g);
}

function boxAt(material, w, h, d, x, y, z, shadow = false) {
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), material);
  m.position.set(x, y, z);
  m.castShadow = shadow;
  return m;
}

// ── MOTORS ───────────────────────────────────────────

function addMotorMeshes(part, scale) {
  const color    = part.color || '#2a2a2a';
  const positions = [ATTACH.motor_fl, ATTACH.motor_fr, ATTACH.motor_rl, ATTACH.motor_rr];
  const g = new THREE.Group();
  positions.forEach(pos => {
    const m = makeMotor(color, scale);
    m.position.copy(pos);
    g.add(m);
  });
  add('motor', g);
}

function makeMotor(color, scale) {
  const g = new THREE.Group();

  // Stator base
  const base = new THREE.Mesh(
    new THREE.CylinderGeometry(1.3 * scale, 1.3 * scale, 0.55, 16),
    mat('#111', { roughness: 0.5, metalness: 0.4 })
  );
  base.castShadow = true;
  g.add(base);

  // Bell (rotating can)
  const bell = new THREE.Mesh(
    new THREE.CylinderGeometry(1.18 * scale, 1.28 * scale, 1.9 * scale, 20),
    mat(color, { roughness: 0.18, metalness: 0.92 })
  );
  bell.position.y = 1.0;
  bell.castShadow = true;
  g.add(bell);

  // Top cap
  const cap = new THREE.Mesh(
    new THREE.CylinderGeometry(1.15 * scale, 1.18 * scale, 0.22, 20),
    mat(color, { roughness: 0.12, metalness: 0.95 })
  );
  cap.position.y = 2.05;
  g.add(cap);

  // Shaft
  const shaft = new THREE.Mesh(
    new THREE.CylinderGeometry(0.22, 0.22, 3.0, 8),
    mat('#aaa', { roughness: 0.08, metalness: 1 })
  );
  shaft.position.y = 1.65;
  g.add(shaft);

  // 4 mount screws
  [0,90,180,270].forEach(deg => {
    const rad = THREE.MathUtils.degToRad(deg);
    const s   = new THREE.Mesh(
      new THREE.CylinderGeometry(0.09, 0.09, 0.32, 6),
      mat('#555', { metalness: 1, roughness: 0.1 })
    );
    s.position.set(Math.cos(rad) * 1.0 * scale, 0.3, Math.sin(rad) * 1.0 * scale);
    g.add(s);
  });

  return g;
}

// ── PROPS ────────────────────────────────────────────

function addPropMeshes(part, scale) {
  const diameter = (part.specs.diameter_inch || 5) * 1.27;
  const blades   = part.specs.blade_count || 3;
  const pScale   = (diameter / 12.7) * scale;
  const positions = [ATTACH.prop_fl, ATTACH.prop_fr, ATTACH.prop_rl, ATTACH.prop_rr];
  const g = new THREE.Group();
  positions.forEach((pos, i) => {
    const p = makeProp(blades, pScale);
    p.position.copy(pos);
    g.add(p);
  });
  add('propeller', g);
}

function makeProp(blades, scale) {
  const g    = new THREE.Group();
  const bMat = mat('#111111', { roughness: 0.55, metalness: 0.08 });

  for (let i = 0; i < blades; i++) {
    const angle = (i / blades) * Math.PI * 2;

    // Tapered blade via ExtrudeGeometry
    const shape = new THREE.Shape();
    shape.moveTo(-0.3, 0);
    shape.quadraticCurveTo(-0.5, 2.2 * scale, -0.15 * scale, 4.6 * scale);
    shape.lineTo( 0.15 * scale, 4.6 * scale);
    shape.quadraticCurveTo( 0.5, 2.2 * scale, 0.3, 0);
    shape.closePath();

    const geo = new THREE.ExtrudeGeometry(shape, {
      depth: 0.07,
      bevelEnabled: true,
      bevelThickness: 0.025,
      bevelSize: 0.025,
      bevelSegments: 1,
    });
    geo.rotateX(-Math.PI / 2);

    const blade = new THREE.Mesh(geo, bMat);
    blade.rotation.y  = angle;
    blade.position.set(0, 0, 0);
    blade.castShadow  = true;
    g.add(blade);
  }

  // Hub
  g.add(Object.assign(
    new THREE.Mesh(
      new THREE.CylinderGeometry(0.38, 0.38, 0.3, 10),
      mat('#333', { metalness: 0.82, roughness: 0.18 })
    ),
    {}
  ));

  return g;
}

// ── ESC ──────────────────────────────────────────────

function addESCMesh(part) {
  const sz = part.specs.form_factor_mm === 20 ? 2.6 : 3.9;
  const g  = new THREE.Group();

  // PCB
  g.add(boxAt(mat('#003311', { roughness: 0.85, metalness: 0.05 }), sz * 2, 0.22, sz * 2, 0, 0, 0, true));

  // MOSFETs at corners
  [[-sz*0.62,-sz*0.62],[sz*0.62,-sz*0.62],[-sz*0.62,sz*0.62],[sz*0.62,sz*0.62]].forEach(([x,z]) => {
    g.add(boxAt(mat('#111', { roughness: 0.35, metalness: 0.65 }), 0.92, 0.44, 0.68, x, 0.33, z));
  });

  // Capacitor
  const cap = new THREE.Mesh(
    new THREE.CylinderGeometry(0.28, 0.28, 0.9, 8),
    mat('#222255', { roughness: 0.6, metalness: 0.1 })
  );
  cap.position.set(-sz * 0.2, 0.56, -sz * 0.2);
  g.add(cap);

  g.position.copy(ATTACH.esc);
  add('esc', g);
}

// ── FC ───────────────────────────────────────────────

function addFCMesh(part) {
  const sz = part.specs.form_factor_mm === 20 ? 2.2 : 3.4;
  const g  = new THREE.Group();

  // PCB
  g.add(boxAt(mat('#000044', { roughness: 0.7, metalness: 0.15 }), sz * 2, 0.18, sz * 2, 0, 0, 0, true));

  // Gyro chip (center)
  g.add(boxAt(mat('#1a1a44', { roughness: 0.25, metalness: 0.55 }), 0.85, 0.14, 0.85, 0, 0.16, 0));

  // USB port
  g.add(boxAt(mat('#888', { roughness: 0.2, metalness: 0.9 }), 0.55, 0.35, 0.22, sz * 0.85, 0.18, 0));

  // LED — cyan glow
  const ledMat = mat('#001133', { roughness: 0, metalness: 0.1, emissive: 0x00c8ff, emissiveIntensity: 2.5 });
  g.add(boxAt(ledMat, 0.2, 0.1, 0.2, sz * 0.7, 0.19, sz * 0.7));

  // Status LED — green
  const grnMat = mat('#001a00', { roughness: 0, metalness: 0, emissive: 0x00ff44, emissiveIntensity: 1.8 });
  g.add(boxAt(grnMat, 0.15, 0.1, 0.15, -sz * 0.7, 0.19, sz * 0.7));

  g.position.copy(ATTACH.fc);
  add('fc', g);
}

// ── CAMERA ───────────────────────────────────────────

function addCameraMesh(part, scale) {
  const g = new THREE.Group();

  // Body
  g.add(boxAt(mat('#111', { roughness: 0.5, metalness: 0.55 }), 1.5, 1.45, 1.8, 0, 0, 0, true));

  // Lens barrel
  const barrel = new THREE.Mesh(
    new THREE.CylinderGeometry(0.48, 0.5, 0.38, 18),
    mat('#1a1a1a', { roughness: 0.18, metalness: 0.8 })
  );
  barrel.rotation.x = Math.PI / 2;
  barrel.position.z = -1.1;
  g.add(barrel);

  // Glass
  const glassMat = new THREE.MeshStandardMaterial({
    color: 0x001122,
    roughness: 0,
    metalness: 0.05,
    transparent: true,
    opacity: 0.72,
  });
  glassMat.userData.origEmissive = 0;
  glassMat.userData.origEmissiveIntensity = 0;
  const glass = new THREE.Mesh(new THREE.CircleGeometry(0.41, 18), glassMat);
  glass.rotation.y = Math.PI;
  glass.position.z = -1.3;
  g.add(glass);

  // Lens reflection ring
  g.add(Object.assign(
    new THREE.Mesh(
      new THREE.TorusGeometry(0.32, 0.04, 6, 18),
      mat('#aaa', { roughness: 0.05, metalness: 1 })
    ),
    { rotation: { x: Math.PI / 2 }, position: new THREE.Vector3(0, 0, -1.28) }
  ));

  const pos = ATTACH.camera.clone();
  pos.x *= scale; pos.z *= scale;
  pos.y = ATTACH.camera.y;
  g.position.copy(pos);
  g.rotation.x = 0.32;
  add('camera', g);
}

// ── VTX ──────────────────────────────────────────────

function addVTXMesh(part) {
  const g = new THREE.Group();

  // PCB
  g.add(boxAt(mat('#221100', { roughness: 0.72, metalness: 0.18 }), 2.5, 0.28, 2.5, 0, 0, 0, true));

  // Heatsink fins
  for (let i = -1; i <= 1; i++) {
    g.add(boxAt(mat('#555', { roughness: 0.3, metalness: 0.8 }), 0.08, 0.55, 1.6, i * 0.5, 0.42, 0));
  }

  // Antenna wire + tip
  const antennaColors = { Analog: '#888', Digital: '#aaa' };
  const aColor = antennaColors[part.specs.protocol] || '#888';
  const ant = new THREE.Mesh(
    new THREE.CylinderGeometry(0.07, 0.07, 4.2, 6),
    mat(aColor, { roughness: 0.2, metalness: 0.9 })
  );
  ant.position.set(0.7, 2.35, 0);
  ant.rotation.z = 0.18;
  g.add(ant);

  // Mushroom antenna tip
  const tip = new THREE.Mesh(
    new THREE.CylinderGeometry(0.28, 0.07, 0.5, 8),
    mat(aColor, { roughness: 0.15, metalness: 0.95 })
  );
  tip.position.set(0.7 + Math.sin(0.18) * 2.1, 4.6, 0);
  g.add(tip);

  // Status LED
  const ledMat = mat('#330000', { roughness: 0, metalness: 0, emissive: 0xff2200, emissiveIntensity: 2 });
  g.add(boxAt(ledMat, 0.18, 0.1, 0.18, -0.8, 0.24, 0.8));

  g.position.copy(ATTACH.vtx);
  add('vtx', g);
}

// ── BATTERY ──────────────────────────────────────────

function addBatteryMesh(part) {
  const cells    = part.specs.cell_count_s || 4;
  const capacity = part.specs.capacity_mah || 1500;
  const len  = 9 + Math.min((capacity - 850) / 600, 5);
  const w    = 3.0 + cells * 0.42;
  const h    = 2.0 + cells * 0.22;
  const g    = new THREE.Group();

  // Main body
  g.add(boxAt(
    mat(part.color || '#1a0000', { roughness: 0.72, metalness: 0.06 }),
    w, h, Math.min(len, 14),
    0, 0, 0, true
  ));

  // Label strip
  g.add(boxAt(
    mat('#fff', { roughness: 0.9, metalness: 0 }),
    w - 0.2, 0.15, Math.min(len, 14) * 0.6,
    0, h / 2 + 0.08, 0
  ));

  // XT60 plug
  const xt60 = new THREE.Group();
  xt60.add(boxAt(mat('#cc8800', { roughness: 0.2, metalness: 0.9 }), 1.3, 1.0, 0.65, 0, 0, 0));
  // Two pin holes
  [-0.3, 0.3].forEach(ox => {
    xt60.add(boxAt(mat('#111', { roughness: 1, metalness: 0 }), 0.22, 0.22, 0.45, ox, -0.08, 0));
  });
  xt60.position.z = -Math.min(len, 14) / 2 - 0.33;
  g.add(xt60);

  // Cell separation lines
  for (let i = 1; i < cells; i++) {
    g.add(boxAt(
      mat('#000', { roughness: 1, metalness: 0 }),
      w + 0.12, h + 0.12, 0.07,
      0, 0, -Math.min(len, 14) / 2 + (Math.min(len, 14) / cells) * i
    ));
  }

  g.position.copy(ATTACH.battery);
  add('battery', g);
}

// ── RECEIVER ─────────────────────────────────────────

function addReceiverMesh(part) {
  const g = new THREE.Group();

  // PCB
  g.add(boxAt(mat('#1a001a', { roughness: 0.8, metalness: 0.12 }), 1.7, 0.19, 1.3, 0, 0, 0, true));

  // RF chip
  g.add(boxAt(mat('#2a002a', { roughness: 0.4, metalness: 0.5 }), 0.6, 0.15, 0.6, 0, 0.17, 0));

  const freq = part.specs.frequency_mhz || 2400;
  const isUHF = freq < 1000;

  // Antennas
  const antPositions = isUHF ? [0] : [-0.5, 0.5];
  antPositions.forEach(x => {
    const ant = new THREE.Mesh(
      new THREE.CylinderGeometry(0.045, 0.045, isUHF ? 5.5 : 3.8, 4),
      mat('#ff8800', { roughness: 0.35, metalness: 0.1 })
    );
    ant.position.set(x, isUHF ? 3.05 : 2.1, 0);
    ant.rotation.z = x > 0 ? 0.28 : x < 0 ? -0.28 : 0;
    g.add(ant);

    // Dipole tip
    const tip = new THREE.Mesh(
      new THREE.SphereGeometry(0.12, 6, 6),
      mat('#ffaa00', { roughness: 0.2, metalness: 0.8 })
    );
    const tipY = isUHF ? 5.9 : 4.2;
    tip.position.set(x + Math.sin(ant.rotation.z) * tipY * 0.4, tipY, 0);
    g.add(tip);
  });

  g.position.copy(ATTACH.receiver);
  add('receiver', g);
}

// ── Helpers ───────────────────────────────────────────

function updateHint(build) {
  const count = Object.keys(build).length;
  const hint  = document.getElementById('hud-hint');
  if (count === 0) {
    hint.textContent = 'Select a component to begin building';
    hint.classList.remove('hidden');
  } else if (count === 9) {
    hint.textContent = '✓ Build complete';
    hint.classList.remove('hidden');
    setTimeout(() => hint.classList.add('hidden'), 3500);
  } else {
    hint.textContent = `${count} / 9 components selected`;
    hint.classList.remove('hidden');
  }
}

function resize() {
  const parent = renderer.domElement.parentElement;
  renderer.setSize(parent.clientWidth, parent.clientHeight);
  if (camera) {
    camera.aspect = parent.clientWidth / parent.clientHeight;
    camera.updateProjectionMatrix();
  }
}

function resetCamera() {
  camAnim = null;
  startCamAnim(DEFAULT_CAM);
}

function screenshot() {
  renderer.render(scene, camera);
  const link = document.createElement('a');
  link.download = 'fpv-build.png';
  link.href = renderer.domElement.toDataURL('image/png');
  link.click();
}
