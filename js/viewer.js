import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { RoomEnvironment } from 'three/addons/environments/RoomEnvironment.js';
import { on, getState, getPartById } from './store.js';

let scene, camera, renderer, controls;
let droneGroup;
const partMeshes = {};

const ATTACH = {
  frame:    new THREE.Vector3(0,    0,    0),
  motor:    null,
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
let _renderer  = null;

export function getRenderer() { return _renderer; }

// ── Material helpers ─────────────────────────────────
// All use MeshPhysicalMaterial for clearcoat & better PBR.
// userData.origEmissive / origEmissiveIntensity are set for highlightSlot().

function matCF(hex = '#0d0d0d') {
  const m = new THREE.MeshPhysicalMaterial({
    color: new THREE.Color(hex),
    roughness: 0.18,
    metalness: 0.0,
    clearcoat: 1.0,
    clearcoatRoughness: 0.08,
    envMapIntensity: 1.1,
  });
  m.userData.origEmissive = 0; m.userData.origEmissiveIntensity = 0;
  return m;
}

function matMetal(hex, roughness = 0.28) {
  const m = new THREE.MeshPhysicalMaterial({
    color: new THREE.Color(hex),
    roughness,
    metalness: 0.96,
    envMapIntensity: 1.6,
  });
  m.userData.origEmissive = 0; m.userData.origEmissiveIntensity = 0;
  return m;
}

function matAnodized(hex, roughness = 0.22) {
  const m = new THREE.MeshPhysicalMaterial({
    color: new THREE.Color(hex),
    roughness,
    metalness: 0.88,
    clearcoat: 0.55,
    clearcoatRoughness: 0.14,
    envMapIntensity: 1.8,
  });
  m.userData.origEmissive = 0; m.userData.origEmissiveIntensity = 0;
  return m;
}

function matPCB(hex) {
  const m = new THREE.MeshPhysicalMaterial({
    color: new THREE.Color(hex),
    roughness: 0.78,
    metalness: 0.04,
    clearcoat: 0.35,
    clearcoatRoughness: 0.45,
  });
  m.userData.origEmissive = 0; m.userData.origEmissiveIntensity = 0;
  return m;
}

function matPlastic(hex, roughness = 0.58) {
  const m = new THREE.MeshPhysicalMaterial({
    color: new THREE.Color(hex),
    roughness,
    metalness: 0.0,
    clearcoat: 0.45,
    clearcoatRoughness: 0.25,
  });
  m.userData.origEmissive = 0; m.userData.origEmissiveIntensity = 0;
  return m;
}

function matGlass() {
  const m = new THREE.MeshPhysicalMaterial({
    color: 0x001a2e,
    roughness: 0.04,
    metalness: 0.0,
    transmission: 0.55,
    transparent: true,
    opacity: 0.82,
    ior: 1.5,
    thickness: 0.2,
    envMapIntensity: 2.0,
  });
  m.userData.origEmissive = 0; m.userData.origEmissiveIntensity = 0;
  return m;
}

function matEmissive(baseHex, emissiveHex, intensity = 2.2) {
  const m = new THREE.MeshPhysicalMaterial({
    color: new THREE.Color(baseHex),
    roughness: 0.1,
    metalness: 0.05,
    emissive: new THREE.Color(emissiveHex),
    emissiveIntensity: intensity,
  });
  m.userData.origEmissive    = emissiveHex;
  m.userData.origEmissiveIntensity = intensity;
  return m;
}

// ── Init ─────────────────────────────────────────────

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
  renderer.toneMappingExposure = 1.05;
  resize();

  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0c0c18);
  scene.fog = new THREE.FogExp2(0x0c0c18, 0.006);

  // PBR environment — dramatically improves metallic/clearcoat materials
  const pmrem = new THREE.PMREMGenerator(renderer);
  pmrem.compileEquirectangularShader();
  scene.environment = pmrem.fromScene(new RoomEnvironment(), 0.06).texture;
  pmrem.dispose();

  camera = new THREE.PerspectiveCamera(48, 1, 0.1, 500);
  camera.position.copy(DEFAULT_CAM.pos);

  controls = new OrbitControls(camera, renderer.domElement);
  controls.enableDamping  = true;
  controls.dampingFactor  = 0.055;
  controls.minDistance    = 8;
  controls.maxDistance    = 90;
  controls.maxPolarAngle  = Math.PI * 0.84;
  controls.target.copy(DEFAULT_CAM.look);

  renderer.domElement.addEventListener('pointerdown', () => { camAnim = null; });

  // ── Lighting (studio 3-point) ────────────────────
  // Environment handles ambient; lights add directionality.
  const ambient = new THREE.AmbientLight(0x0a0818, 1.2);
  scene.add(ambient);

  // Key — warm, high front-right
  const key = new THREE.DirectionalLight(0xfff5e8, 2.8);
  key.position.set(22, 44, 26);
  key.castShadow = true;
  key.shadow.mapSize.set(2048, 2048);
  key.shadow.bias = -0.0008;
  Object.assign(key.shadow.camera, { near: 1, far: 110, left: -30, right: 30, top: 30, bottom: -30 });
  scene.add(key);

  // Fill — cool blue, left side
  const fill = new THREE.DirectionalLight(0x8ab4ff, 0.55);
  fill.position.set(-24, 10, -16);
  scene.add(fill);

  // Rim — cyan edge from behind-below
  const rim = new THREE.DirectionalLight(0x00e8ff, 0.9);
  rim.position.set(0, -5, -30);
  scene.add(rim);

  // ── Ground (reflective studio floor) ────────────
  const groundMat = new THREE.MeshStandardMaterial({
    color: 0x060610,
    roughness: 0.08,
    metalness: 0.85,
    envMapIntensity: 0.55,
  });
  groundMat.userData.origEmissive = 0;
  groundMat.userData.origEmissiveIntensity = 0;
  const ground = new THREE.Mesh(new THREE.PlaneGeometry(100, 100), groundMat);
  ground.rotation.x = -Math.PI / 2;
  ground.position.y = -6;
  ground.receiveShadow = true;
  scene.add(ground);

  // Subtle grid overlay on ground
  const grid = new THREE.GridHelper(80, 40, 0x12122a, 0x0e0e22);
  grid.position.y = -5.98;
  scene.add(grid);

  droneGroup = new THREE.Group();
  scene.add(droneGroup);

  renderer._scene  = scene;
  renderer._camera = camera;

  let t = 0;
  const idle = () => {
    t += 0.006;
    droneGroup.position.y = Math.sin(t) * 0.25;
    droneGroup.rotation.y = Math.sin(t * 0.32) * 0.03;
  };

  (function loop() {
    requestAnimationFrame(loop);

    if (camAnim) {
      const raw  = Math.min((performance.now() - camAnim.start) / camAnim.dur, 1);
      const ease = 1 - Math.pow(1 - raw, 3);
      camera.position.lerpVectors(camAnim.fromPos, camAnim.toPos, ease);
      controls.target.lerpVectors(camAnim.fromLook, camAnim.toLook, ease);
      if (raw >= 1) camAnim = null;
    }

    const { build } = getState();
    if (partMeshes.propeller && build.motor) {
      partMeshes.propeller.children.forEach((pg, i) => {
        pg.rotation.y += i % 2 === 0 ? 0.20 : -0.20;
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
    dur:      680,
  };
}

// ── Slot highlighting ────────────────────────────────

function highlightSlot(slotKey) {
  Object.values(partMeshes).forEach(mesh => {
    if (!mesh) return;
    mesh.traverse(child => {
      if (!child.isMesh || !child.material) return;
      const ud = child.material.userData;
      child.material.emissive?.set(ud.origEmissive || 0);
      if (child.material.emissiveIntensity !== undefined)
        child.material.emissiveIntensity = ud.origEmissiveIntensity ?? 0;
    });
  });

  const target = partMeshes[slotKey];
  if (!slotKey || !target) return;

  target.traverse(child => {
    if (!child.isMesh || !child.material) return;
    child.material.emissive?.setHex(0x00b8f0);
    if (child.material.emissiveIntensity !== undefined)
      child.material.emissiveIntensity = 0.5;
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

  if (activeSlot) highlightSlot(activeSlot);
  updateHint(build);
}

function clearAll() {
  Object.values(partMeshes).forEach(m => { if (m) droneGroup.remove(m); });
  Object.keys(partMeshes).forEach(k => delete partMeshes[k]);
}

// ── Pop-in animation ─────────────────────────────────

function popIn(mesh) {
  mesh.scale.setScalar(0.01);
  droneGroup.add(mesh);
  const start = performance.now(), dur = 420;
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

function boxAt(material, w, h, d, x, y, z, shadow = false) {
  const m = new THREE.Mesh(new THREE.BoxGeometry(w, h, d), material);
  m.position.set(x, y, z);
  m.castShadow   = shadow;
  m.receiveShadow = shadow;
  return m;
}

// ── FRAME ────────────────────────────────────────────

function addFrameMesh(part, scale) {
  const color  = part.color || '#141414';
  const cfMat  = matCF(color);
  const cfThin = matCF(color);
  const stnMat = matMetal('#3a3a3a', 0.22);
  const ringMat = matMetal('#555', 0.18);

  const g = new THREE.Group();

  // Bottom center plate
  const bot = boxAt(cfMat, 7 * scale, 0.8, 5 * scale, 0, -0.4, 0, true);
  // Round the feel with a subtle bevel by stacking two boxes
  g.add(bot);

  // Top plate
  g.add(boxAt(cfThin, 5 * scale, 0.45, 4 * scale, 0, 1.2, 0, true));

  // 4 arms — X pattern
  const armLen = 11.5 * scale;
  [[-1,-1],[1,-1],[-1,1],[1,1]].forEach(([dx, dz]) => {
    const arm = boxAt(cfMat, armLen, 0.5, 1.4 * scale,
      dx * armLen * 0.42, 0, dz * armLen * 0.42, true);
    arm.rotation.y = Math.atan2(dz, dx);
    g.add(arm);

    // Arm taper: thin carbon overlay on top
    const top = boxAt(cfThin, armLen * 0.85, 0.2, 1.0 * scale,
      dx * armLen * 0.42, 0.35, dz * armLen * 0.42);
    top.rotation.y = Math.atan2(dz, dx);
    g.add(top);
  });

  // Standoff columns (4×)
  [-1.9, 1.9].forEach(sx => [-1.5, 1.5].forEach(sz => {
    const cyl = new THREE.Mesh(
      new THREE.CylinderGeometry(0.22, 0.22, 1.65, 8),
      stnMat
    );
    cyl.castShadow = true;
    cyl.position.set(sx * scale, 0.45, sz * scale);
    g.add(cyl);

    // Standoff nuts top/bottom
    [0.05, 1.25].forEach(y => {
      const nut = new THREE.Mesh(
        new THREE.CylinderGeometry(0.3, 0.3, 0.18, 6),
        stnMat
      );
      nut.position.set(sx * scale, -0.4 + y, sz * scale);
      g.add(nut);
    });
  }));

  // Motor-mount rings at arm tips
  [ATTACH.motor_fl, ATTACH.motor_fr, ATTACH.motor_rl, ATTACH.motor_rr].forEach(pos => {
    const ring = new THREE.Mesh(
      new THREE.TorusGeometry(1.45 * scale, 0.14, 8, 18),
      ringMat
    );
    ring.rotation.x = Math.PI / 2;
    ring.position.copy(pos);
    g.add(ring);

    // Arm-tip plate
    g.add(boxAt(cfMat, 2.6 * scale, 0.45, 2.6 * scale, pos.x, pos.y, pos.z));
  });

  add('frame', g);
}

// ── MOTORS ───────────────────────────────────────────

function addMotorMeshes(part, scale) {
  const color     = part.color || '#2a2a2a';
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
  const g       = new THREE.Group();
  const baseMat = matMetal('#1a1a1a', 0.45);
  const bellMat = matAnodized(color, 0.18);
  const capMat  = matAnodized(color, 0.12);
  const shaftMat = matMetal('#c0c0c0', 0.08);
  const screwMat = matMetal('#444', 0.15);

  // Stator/base ring
  const base = new THREE.Mesh(
    new THREE.CylinderGeometry(1.38 * scale, 1.38 * scale, 0.62, 18),
    baseMat
  );
  base.castShadow = true;
  g.add(base);

  // Stator teeth (simplified as a slightly smaller cylinder with different mat)
  const stator = new THREE.Mesh(
    new THREE.CylinderGeometry(1.1 * scale, 1.1 * scale, 0.55, 12),
    matMetal('#222', 0.6)
  );
  stator.position.y = 0.04;
  g.add(stator);

  // Bell (rotating can) — slightly tapered
  const bell = new THREE.Mesh(
    new THREE.CylinderGeometry(1.22 * scale, 1.32 * scale, 2.0 * scale, 22),
    bellMat
  );
  bell.position.y = 1.05;
  bell.castShadow = true;
  g.add(bell);

  // Bell top cap
  const cap = new THREE.Mesh(
    new THREE.CylinderGeometry(1.18 * scale, 1.22 * scale, 0.24, 22),
    capMat
  );
  cap.position.y = 2.13;
  g.add(cap);

  // Center shaft
  const shaft = new THREE.Mesh(
    new THREE.CylinderGeometry(0.24, 0.24, 3.2, 8),
    shaftMat
  );
  shaft.position.y = 1.7;
  shaft.castShadow = true;
  g.add(shaft);

  // Mount screws at 90° intervals
  for (let i = 0; i < 4; i++) {
    const rad = (i / 4) * Math.PI * 2;
    const screw = new THREE.Mesh(
      new THREE.CylinderGeometry(0.1, 0.1, 0.38, 6),
      screwMat
    );
    screw.position.set(Math.cos(rad) * 1.05 * scale, 0.22, Math.sin(rad) * 1.05 * scale);
    g.add(screw);

    // Screw head
    const head = new THREE.Mesh(
      new THREE.CylinderGeometry(0.18, 0.18, 0.1, 6),
      screwMat
    );
    head.position.set(Math.cos(rad) * 1.05 * scale, 0.44, Math.sin(rad) * 1.05 * scale);
    g.add(head);
  }

  return g;
}

// ── PROPELLERS ───────────────────────────────────────

function addPropMeshes(part, scale) {
  const diameter = (part.specs.diameter_inch || 5) * 1.27;
  const blades   = part.specs.blade_count || 3;
  const pScale   = (diameter / 12.7) * scale;
  const positions = [ATTACH.prop_fl, ATTACH.prop_fr, ATTACH.prop_rl, ATTACH.prop_rr];
  const g = new THREE.Group();
  positions.forEach((pos) => {
    const p = makeProp(blades, pScale);
    p.position.copy(pos);
    g.add(p);
  });
  add('propeller', g);
}

function makeProp(blades, scale) {
  const g    = new THREE.Group();
  const bMat = matPlastic('#0e0e0e', 0.5);
  const hubMat = matMetal('#2a2a2a', 0.35);

  for (let i = 0; i < blades; i++) {
    const angle = (i / blades) * Math.PI * 2;

    const shape = new THREE.Shape();
    shape.moveTo(-0.32, 0);
    shape.quadraticCurveTo(-0.55, 2.4 * scale, -0.12 * scale, 5.0 * scale);
    shape.lineTo( 0.12 * scale, 5.0 * scale);
    shape.quadraticCurveTo( 0.55, 2.4 * scale, 0.32, 0);
    shape.closePath();

    const geo = new THREE.ExtrudeGeometry(shape, {
      depth: 0.08,
      bevelEnabled: true,
      bevelThickness: 0.03,
      bevelSize: 0.03,
      bevelSegments: 2,
    });
    geo.rotateX(-Math.PI / 2);

    const blade = new THREE.Mesh(geo, bMat);
    blade.rotation.y  = angle;
    blade.castShadow  = true;
    g.add(blade);
  }

  // Hub cylinder
  const hub = new THREE.Mesh(
    new THREE.CylinderGeometry(0.42, 0.42, 0.34, 12),
    hubMat
  );
  g.add(hub);

  // Shaft collar
  const collar = new THREE.Mesh(
    new THREE.CylinderGeometry(0.2, 0.2, 0.55, 8),
    matMetal('#bbb', 0.1)
  );
  collar.position.y = 0.1;
  g.add(collar);

  return g;
}

// ── ESC ──────────────────────────────────────────────

function addESCMesh(part) {
  const sz  = part.specs.form_factor_mm === 20 ? 2.8 : 4.0;
  const g   = new THREE.Group();
  const pcb = matPCB('#001a08');

  // PCB
  g.add(boxAt(pcb, sz * 2, 0.24, sz * 2, 0, 0, 0, true));

  // Corner MOSFET chips
  [[-sz*0.6,-sz*0.6],[sz*0.6,-sz*0.6],[-sz*0.6,sz*0.6],[sz*0.6,sz*0.6]].forEach(([x,z]) => {
    g.add(boxAt(matMetal('#1a1a1a', 0.4), 1.0, 0.48, 0.72, x, 0.36, z));
    // Thermal pad
    g.add(boxAt(matMetal('#333', 0.6), 0.75, 0.14, 0.55, x, 0.56, z));
  });

  // Bulk capacitor
  const cap = new THREE.Mesh(
    new THREE.CylinderGeometry(0.32, 0.32, 1.0, 10),
    matPlastic('#1a1a44', 0.7)
  );
  cap.position.set(-sz * 0.22, 0.62, -sz * 0.22);
  cap.castShadow = true;
  g.add(cap);

  // Capacitor stripe
  const stripe = new THREE.Mesh(
    new THREE.CylinderGeometry(0.33, 0.33, 0.18, 10),
    matPlastic('#aaaacc', 0.8)
  );
  stripe.position.set(-sz * 0.22, 1.1, -sz * 0.22);
  g.add(stripe);

  // Phase wire pads (solder points)
  ['#aa4400','#cc6600','#884400'].forEach((col, i) => {
    g.add(boxAt(matMetal(col, 0.5), 0.28, 0.16, 0.22, sz * 0.72, 0.2, -sz * 0.5 + i * sz * 0.5));
  });

  g.position.copy(ATTACH.esc);
  add('esc', g);
}

// ── FLIGHT CONTROLLER ────────────────────────────────

function addFCMesh(part) {
  const sz  = part.specs.form_factor_mm === 20 ? 2.4 : 3.5;
  const g   = new THREE.Group();
  const pcb = matPCB('#00004a');

  // PCB
  g.add(boxAt(pcb, sz * 2, 0.2, sz * 2, 0, 0, 0, true));

  // Gyro IC (center)
  g.add(boxAt(matMetal('#111130', 0.35), 0.9, 0.16, 0.9, 0, 0.18, 0));

  // CPU / MCU
  g.add(boxAt(matMetal('#0a0a1a', 0.4), 0.65, 0.13, 0.65, sz * 0.45, 0.165, -sz * 0.45));

  // USB-C port
  g.add(boxAt(matMetal('#888', 0.18), 0.62, 0.38, 0.24, sz * 0.9, 0.19, 0));

  // Capacitors (2 small)
  [sz*0.4, -sz*0.4].forEach(xp => {
    const c = new THREE.Mesh(
      new THREE.CylinderGeometry(0.16, 0.16, 0.55, 8),
      matPlastic('#111144', 0.75)
    );
    c.position.set(xp, 0.37, sz * 0.7);
    g.add(c);
  });

  // Status LEDs
  g.add(boxAt(matEmissive('#001133', '#00ccff', 2.8), 0.22, 0.08, 0.22, sz * 0.72, 0.15, sz * 0.72));
  g.add(boxAt(matEmissive('#001800', '#00ff55', 2.2), 0.18, 0.08, 0.18, -sz * 0.72, 0.15, sz * 0.72));
  g.add(boxAt(matEmissive('#220000', '#ff2200', 1.8), 0.16, 0.08, 0.16, sz * 0.72, 0.15, -sz * 0.72));

  // Corner mounting holes
  [-1,1].forEach(sx => [-1,1].forEach(sz2 => {
    const hole = new THREE.Mesh(
      new THREE.CylinderGeometry(0.18, 0.18, 0.25, 8),
      matMetal('#333', 0.3)
    );
    hole.position.set(sx * sz * 0.82, 0.1, sz2 * sz * 0.82);
    g.add(hole);
  }));

  g.position.copy(ATTACH.fc);
  add('fc', g);
}

// ── FPV CAMERA ───────────────────────────────────────

function addCameraMesh(part, scale) {
  const g = new THREE.Group();

  // Housing
  g.add(boxAt(matMetal('#0e0e0e', 0.55), 1.6, 1.55, 1.85, 0, 0, 0, true));

  // Side grille details
  [-0.72, 0.72].forEach(x => {
    for (let i = -2; i <= 2; i++) {
      g.add(boxAt(matMetal('#1a1a1a', 0.7), 0.08, 0.2, 1.2, x, i * 0.22, 0));
    }
  });

  // Lens barrel
  const barrel = new THREE.Mesh(
    new THREE.CylinderGeometry(0.52, 0.54, 0.44, 20),
    matMetal('#1e1e1e', 0.22)
  );
  barrel.rotation.x = Math.PI / 2;
  barrel.position.z = -1.15;
  barrel.castShadow = true;
  g.add(barrel);

  // Lens glass
  const glass = new THREE.Mesh(new THREE.CircleGeometry(0.44, 22), matGlass());
  glass.rotation.y = Math.PI;
  glass.position.z = -1.38;
  g.add(glass);

  // Lens reflection ring (bright chrome)
  const ring1 = new THREE.Mesh(
    new THREE.TorusGeometry(0.44, 0.05, 8, 22),
    matMetal('#d0d0d0', 0.06)
  );
  ring1.rotation.x = Math.PI / 2;
  ring1.position.z = -1.36;
  g.add(ring1);

  // Inner ring
  const ring2 = new THREE.Mesh(
    new THREE.TorusGeometry(0.32, 0.03, 6, 18),
    matMetal('#888', 0.12)
  );
  ring2.rotation.x = Math.PI / 2;
  ring2.position.z = -1.37;
  g.add(ring2);

  // Status LED
  g.add(boxAt(matEmissive('#001800', '#00ff44', 1.8), 0.14, 0.08, 0.14, 0.65, 0.62, -0.85));

  const pos = ATTACH.camera.clone();
  pos.x *= scale; pos.z *= scale;
  pos.y  = ATTACH.camera.y;
  g.position.copy(pos);
  g.rotation.x = 0.3;
  add('camera', g);
}

// ── VIDEO TRANSMITTER ─────────────────────────────────

function addVTXMesh(part) {
  const g = new THREE.Group();
  const isDigital = part.specs.protocol === 'Digital';

  // PCB
  g.add(boxAt(matPCB('#1a0a00'), 2.6, 0.3, 2.6, 0, 0, 0, true));

  // IC chip
  g.add(boxAt(matMetal('#111', 0.4), 0.9, 0.18, 0.9, 0, 0.24, 0));

  // Heatsink fins
  for (let i = -2; i <= 2; i++) {
    g.add(boxAt(matMetal('#555', 0.28), 0.1, 0.6, 1.8, i * 0.38, 0.45, 0));
  }
  // Heatsink base
  g.add(boxAt(matMetal('#444', 0.32), 2.0, 0.18, 1.85, 0, 0.3, 0));

  // Antenna
  const antColor = isDigital ? '#c0c0c0' : '#808080';
  const antMat   = matMetal(antColor, 0.2);
  const antH     = isDigital ? 5.0 : 4.0;

  const ant = new THREE.Mesh(
    new THREE.CylinderGeometry(0.08, 0.08, antH, 8),
    antMat
  );
  ant.position.set(0.8, antH / 2 + 0.3, 0);
  ant.rotation.z = 0.15;
  ant.castShadow = true;
  g.add(ant);

  // Mushroom tip
  const tip = new THREE.Mesh(
    new THREE.CylinderGeometry(0.32, 0.08, 0.6, 10),
    antMat
  );
  tip.position.set(0.8 + Math.sin(0.15) * (antH + 0.3), antH + 0.3, 0);
  g.add(tip);

  // Connector
  g.add(boxAt(matMetal('#888', 0.15), 0.55, 0.4, 0.55, -0.9, 0.35, 0));

  // Status LED
  g.add(boxAt(matEmissive('#1a0000', '#ff2200', 2.2), 0.2, 0.1, 0.2, -0.85, 0.26, 0.85));

  g.position.copy(ATTACH.vtx);
  add('vtx', g);
}

// ── BATTERY ──────────────────────────────────────────

function addBatteryMesh(part) {
  const cells    = part.specs.cell_count_s || 4;
  const capacity = part.specs.capacity_mah || 1500;
  const len  = Math.min(8.5 + (capacity - 850) / 500, 14);
  const w    = 3.0 + cells * 0.44;
  const h    = 1.9 + cells * 0.24;
  const g    = new THREE.Group();

  const bodyColor = part.color || '#1a0000';
  const bodyMat   = matPlastic(bodyColor, 0.65);
  const wrapMat   = matPlastic(bodyColor, 0.72);

  // Main cell wrap
  g.add(boxAt(bodyMat, w, h, len, 0, 0, 0, true));

  // Subtle cell separation grooves
  for (let i = 1; i < cells; i++) {
    const segLen = len / cells;
    g.add(boxAt(wrapMat, w + 0.02, h + 0.02, 0.08,
      0, 0, -len / 2 + segLen * i));
  }

  // Label / branding strip
  g.add(boxAt(
    matPlastic('#f0f0f0', 0.9),
    w - 0.1, 0.06, len * 0.55,
    0, h / 2 + 0.04, 0
  ));

  // XT60 connector housing
  const xt60 = new THREE.Group();
  g.add(xt60);
  xt60.position.z = -len / 2 - 0.4;

  const housing = boxAt(matPlastic('#cc8800', 0.35), 1.4, 1.1, 0.7, 0, 0, 0);
  xt60.add(housing);

  // Pin holes
  [-0.32, 0.32].forEach(ox => {
    xt60.add(boxAt(matPlastic('#111', 0.9), 0.24, 0.26, 0.5, ox, -0.06, 0));
  });

  // Balance lead wires (simplified)
  const wireMat = matPlastic('#222', 0.85);
  g.add(boxAt(wireMat, 0.18, 0.18, 2.8, w / 2 + 0.12, h * 0.3, -len * 0.3));

  g.position.copy(ATTACH.battery);
  add('battery', g);
}

// ── RC RECEIVER ──────────────────────────────────────

function addReceiverMesh(part) {
  const g   = new THREE.Group();
  const freq = part.specs.frequency_mhz || 2400;
  const isUHF = freq < 1000;

  // PCB
  g.add(boxAt(matPCB('#1a001a'), 1.8, 0.2, 1.4, 0, 0, 0, true));

  // RF chip
  g.add(boxAt(matMetal('#2a002a', 0.45), 0.65, 0.16, 0.65, 0, 0.18, 0));

  // Crystal oscillator
  g.add(boxAt(matMetal('#888', 0.25), 0.22, 0.32, 0.12, 0.5, 0.26, -0.3));

  // Shield can
  g.add(boxAt(matMetal('#333', 0.28), 0.85, 0.28, 0.85, -0.3, 0.24, 0.25));

  // Antennas
  const antColor   = '#ff8c00';
  const antPositions = isUHF ? [[0, 0]] : [[-0.55, 0], [0.55, 0]];
  const antH         = isUHF ? 6.0 : 4.0;

  antPositions.forEach(([x, z]) => {
    const ant = new THREE.Mesh(
      new THREE.CylinderGeometry(0.05, 0.05, antH, 5),
      matPlastic(antColor, 0.4)
    );
    ant.position.set(x, antH / 2 + 0.2, z);
    const lean = x > 0 ? 0.28 : x < 0 ? -0.28 : 0;
    ant.rotation.z = lean;
    ant.castShadow = true;
    g.add(ant);

    const tipY = antH + 0.2 + Math.cos(Math.abs(lean)) * antH * 0.5;
    const tipX = x + Math.sin(lean) * antH * 0.5;
    const tip = new THREE.Mesh(
      new THREE.SphereGeometry(0.14, 7, 7),
      matMetal('#ffaa00', 0.2)
    );
    tip.position.set(tipX, tipY, z);
    g.add(tip);
  });

  // Bind button
  g.add(boxAt(matPlastic('#ff4444', 0.5), 0.22, 0.18, 0.22, -0.65, 0.19, -0.5));

  g.position.copy(ATTACH.receiver);
  add('receiver', g);
}

// ── Helpers ──────────────────────────────────────────

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
  const link      = document.createElement('a');
  link.download   = 'fpv-build.png';
  link.href       = renderer.domElement.toDataURL('image/png');
  link.click();
}
