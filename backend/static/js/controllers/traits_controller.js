Traits.TraitsController = Ember.ArrayController.extend({
	inputValue: '@',
	displayResults: false,
	actions: {
		sendTwitterHandle: function(){
			var twitterHandle = this.get("inputValue");
			this.toggleProperty('displayResults');
			// this.transitionToRoute('result');
		},
		clickTryAgain: function(){
			this.toggleProperty('displayResults');
		}
	}
});
