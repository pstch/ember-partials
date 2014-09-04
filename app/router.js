import Ember from 'ember';

var Router = Ember.Router.extend({
  location: EmberPartialsENV.locationType
});

Router.map(function() {
    this.route('auth', { path: '/login' });
    this.resource('testobjs', { path: '/' });
    this.resource('testobj', { path: '/:testobj_id' });
});

export default Router;
