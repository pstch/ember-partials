import Ember from 'ember';

export default Ember.Controller.extend({
    username: null,
    password: null,
    token: null,
    errors: null,
    api_host: 'http://localhost:4231',
    actions: {
        login: function() {
            var self = this;
            var data = this.getProperties('username', 'password');
            Ember.$.post(
                this.api_host + '/api/auth/token',
                data, null, 'json').then(
                    function(response) {
                        self.reset();
                        self.set('token', response.token);
                        self.transitionToRoute('');
                    },
                    function(jqXHR) {
                        self.set(
                            'errors',
                            Ember.$.parseJSON(jqXHR.responseText)
                        );
                    }
                );
        }
    },

    reset: function() {
        this.setProperties({
            username: null,
            password: null,
            errors: null,
            model: null
        });
    },

    hasValidToken: function() {
        return this.isTokenValid()
    }.property('token'),

    isTokenValid: function() {
        var token = this.get('token');
        return (!Ember.isEmpty(token) && token != 'null' && token !== 'undefined');
    },

    setupAjax: function() {
        var self = this, token = this.get('token');
        Ember.$(document).ajaxSend(function(event, xhr) {
            if (self.isTokenValid()) {
                xhr.setRequestHeader("Authorization", "Token " + token);
            }
        });
    },

    setCurrentUser: function() {
        if (this.isTokenValid()) {
            var currentUser = this.store.find('auth/user', 'me');
            this.set('model', currentUser);
        } else {
            this.reset();
        }
    },

    tokenChanged: function() {
        localStorage.api_auth_token = this.get('token');
        this.setupAjax();
        this.setCurrentUser();
    }.observes('token')
});
