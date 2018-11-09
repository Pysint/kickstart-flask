// This file should contain all UI triggers ie. clicks and changes
$("#change-example").on('change', exampleChangeFunction);
$("#click-example").on('click', exampleClickFunction);
$("#sidebar-content").on('click', 'a', function(e){
  e.preventDefault();
  var url = $(this).attr('href');
  $('#content-main').load(url);
});
