import { getState, getPartById, dispatch } from './store.js';

export function evaluate() {
  const { build, rules } = getState();
  const violations = [];

  for (const rule of rules) {
    const partA = getPartById(build[rule.slot_a]);
    const partB = getPartById(build[rule.slot_b]);

    if (!partA || !partB) continue;

    const valA = partA.specs[rule.spec_a];
    const valB = partB.specs[rule.spec_b];

    if (valA === undefined || valB === undefined) continue;

    let violated = false;

    if (rule.type === 'spec_match') {
      violated = valA !== valB;
    } else if (rule.type === 'range') {
      switch (rule.operator) {
        case '>=': violated = valA < valB;  break;
        case '<=': violated = valA > valB;  break;
        case '==': violated = valA !== valB; break;
      }
    }

    if (violated) {
      const message = rule.message
        .replace('{a}', valA)
        .replace('{b}', valB);
      violations.push({ id: rule.id, slots: [rule.slot_a, rule.slot_b], message });
    }
  }

  dispatch('SET_VIOLATIONS', { violations });
  return violations;
}

export function slotsWithViolations() {
  const { violations } = getState();
  const bad = new Set();
  violations.forEach(v => v.slots.forEach(s => bad.add(s)));
  return bad;
}
