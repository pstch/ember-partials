import DS from "ember-data";

export default DS.DjangoRESTAdapter.extend({host: 'http://127.0.0.1:4231/api'});
