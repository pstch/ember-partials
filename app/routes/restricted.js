import Ember from 'ember';

export default Ember.Mixin.create({
    beforeModel: function() {
        if (!this.controllerFor('auth').isTokenValid()) {
            this.transitionTo('auth');
        }
    }
});
