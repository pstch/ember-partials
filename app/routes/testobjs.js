import Ember from 'ember';

import Restricted from './restricted';

export default Ember.Route.extend(Restricted, {
  model: function() {
    return this.store.find('testobj');
  }
});
