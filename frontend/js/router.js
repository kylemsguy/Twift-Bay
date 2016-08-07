Traits.Router.map(function() {
  this.resource('traits', { path: '/' });
});

Traits.TraitsRoute = Ember.Route.extend({
	model: function(){
		return this.store.find('trait');
	}
})