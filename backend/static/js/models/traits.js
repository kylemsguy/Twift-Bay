Traits.Trait = DS.Model.extend({
  // inputValue: DS.attr('string'),	
  title: DS.attr('string'),
  isAvailable: DS.attr('boolean'),
  score: DS.attr('string')
});

Traits.Trait.FIXTURES = [
 {
   id: 1,
   title: 'Modest',
   score: 50
 },
 {
   id: 2,
   title: 'Stubborn',
   score: 70
 },
 {
   id: 3,
   title: 'Bashful',
   score: 40
 }
];