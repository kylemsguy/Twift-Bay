Traits.Router.map(function() {
  this.route('traits', { path: '/' });
  // this.route('test', { path: '/test' });
  // this.route('result', { path: '/result' });
  // this.resource('result', { path: '/result/:user_name' });
});

// Traits.ResultRoute = Ember.Route.extend({
// 	model: function(params){
// 		return this.store.find('result', params_user_name);
// 	}
// })

Traits.TraitsRoute = Ember.Route.extend({
	model: function(){
		return this.store.find('trait');
	}
})