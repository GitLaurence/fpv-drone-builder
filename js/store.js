const _state = {
  catalog: [],
  categories: [],
  rules: [],
  presets: {},
  build: {},       // { slotKey: partId }
  activeSlot: null,
  violations: [],
};

const _listeners = {};

export function getState() {
  return _state;
}

export function on(event, fn) {
  if (!_listeners[event]) _listeners[event] = [];
  _listeners[event].push(fn);
}

function emit(event, payload) {
  (_listeners[event] || []).forEach(fn => fn(payload));
}

export function dispatch(event, payload) {
  switch (event) {

    case 'INIT': {
      _state.catalog    = payload.parts;
      _state.categories = payload.categories;
      _state.rules      = payload.compatibility_rules;
      _state.presets    = payload.presets;
      emit('catalog:ready', _state);
      break;
    }

    case 'SET_ACTIVE_SLOT': {
      _state.activeSlot = payload.slot;
      emit('slot:active', { slot: payload.slot });
      break;
    }

    case 'SELECT_PART': {
      const { slot, partId } = payload;
      if (partId === null) {
        delete _state.build[slot];
      } else {
        _state.build[slot] = partId;
      }
      _state.activeSlot = null;
      emit('build:changed', { build: _state.build });
      emit('slot:active', { slot: null });
      break;
    }

    case 'LOAD_PRESET': {
      _state.build = { ...payload.parts };
      _state.activeSlot = null;
      emit('build:changed', { build: _state.build });
      emit('slot:active', { slot: null });
      break;
    }

    case 'RESET_BUILD': {
      _state.build = {};
      _state.activeSlot = null;
      _state.violations = [];
      emit('build:changed', { build: _state.build });
      emit('slot:active', { slot: null });
      break;
    }

    case 'SET_VIOLATIONS': {
      _state.violations = payload.violations;
      emit('violations:updated', { violations: payload.violations });
      break;
    }
  }
}

export function getPartById(id) {
  return _state.catalog.find(p => p.id === id) || null;
}

export function getPartsByCategory(categoryId) {
  return _state.catalog.filter(p => p.category === categoryId);
}

export function getSelectedPart(slotKey) {
  const id = _state.build[slotKey];
  return id ? getPartById(id) : null;
}
