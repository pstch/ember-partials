import Ember from 'ember';

export default Ember.Route.extend({
    init: function() {
        this._super();
        this.controllerFor('auth').set('token', localStorage.api_auth_token);
        this.controllerFor('auth').setupAjax();
        this.controllerFor('auth').setCurrentUser();
    },
    actions: {
        logout: function() {
            this.controllerFor('auth').set('token', null);
            this.transitionTo('');
        }
    }
});
