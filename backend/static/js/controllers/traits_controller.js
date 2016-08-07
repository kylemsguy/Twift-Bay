Traits.TraitsController = Ember.ArrayController.extend({
	inputValue: '@',
	displayResults: false,
	products: null,
	
	// baseImgPath: 'http://ebay.com/p/'
	// computedProp: function() {
	// 	return
	// }
	// personality: [
	// 			{
	// 				"id": "Adventurousness",
	// 				"sampling_error": 0.0494392844,
	// 				"percentage": 0.5815211780249463,
	// 				"name": "Adventurousness",
	// 				"category": "personality"
	// 			},
	// 			{
	// 				"id": "Artistic interests",
	// 				"sampling_error": 0.1009730732,
	// 				"percentage": 0.027685155619603698,
	// 				"name": "Artistic interests",
	// 				"category": "personality"
	// 			},
	// 			{
	// 				"id": "Emotionality",
	// 				"sampling_error": 0.0464381914,
	// 				"percentage": 0.21295364136485728,
	// 				"name": "Emotionality",
	// 				"category": "personality"
	// 			},
	// 			{
	// 				"id": "Imagination",
	// 				"sampling_error": 0.061762134499999996,
	// 				"percentage": 0.869645354683581,
	// 				"name": "Imagination",
	// 				"category": "personality"
	// 			},
	// 			{
	// 				"id": "Intellect",
	// 				"sampling_error": 0.054068624100000004,
	// 				"percentage": 0.8023486487481887,
	// 				"name": "Intellect",
	// 				"category": "personality"
	// 			},
	// 			{
	// 				"id": "Liberalism",
	// 				"sampling_error": 0.0812002711,
	// 				"percentage": 0.8810067929131393,
	// 				"name": "Authority-challenging",
	// 				"category": "personality"
	// 			}
	// 							],
	actions: {
		sendTwitterHandle: function(){
			var self = this;
			var twitterHandle = this.get("inputValue");
			this.toggleProperty('displayResults');
			var endpoint = "/api/suggest-gift?user=" + twitterHandle;
			console.log(endpoint);
			console.log($.getJSON(endpoint));

			$.getJSON(endpoint, function(data){
				self.set('products', data.responseJSON);
			});

			// this.transitionToRoute('result');
		},
		clickTryAgain: function(){
			// this.toggleProperty('displayResults');
			location.reload();
		}
	}
});
