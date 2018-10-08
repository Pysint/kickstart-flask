Handlebars.registerHelper('if_eq', function(a, b, options) {
  if(a === b) {
    return options.fn(this);
  }
  return options.inverse(this);
});

Handlebars.registerHelper('if_neq', function(a, b, options) {
  if(a != b) {
    return options.fn(this);
  }
  return options.inverse(this);
});
