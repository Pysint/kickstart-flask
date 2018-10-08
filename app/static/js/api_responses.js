function LoginResult(apiResult){
  if(apiResult.result == "success"){
    location.href = "/index"
  }
}

function ResponseExample(apiResult){
  // #example-replace-template is the handlebars template in the template file
  var source   = $("#example-replace-template").html();
  var template = Handlebars.compile(source);
  var html = template(context);
  // #example-replace-html is the div ID that should contain the Handlebars
  // content
  $("#example-replace-html").html(html);
}
