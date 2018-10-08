function apiPost(destination, postData, action){
  postData = JSON.stringify(postData);
  $.ajax(
    {
      url : destination,
      type: "POST",
      data: postData,
      contentType: "application/json",
      dataType: "json",
      success:function(json){
        responseAction(json, action);
      },
      error: function(response, status, error){
        console.log(response);
        console.log(status);
      }
    }
  )
}

function apiGet(destination, action){
  $.ajax(
    {
      url : destination,
      type: "GET",
      dataType: "json",
      success:function(json){
        responseAction(json, action);
      },
      error: function(response, status, error){
        console.log(response);
        console.log(status);
      }
    }
  )
}

function apiDelete(destination, action){
  $.ajax(
    {
      url : destination,
      type: "DELETE",
      dataType: "json",
      success:function(json){
        responseAction(json, action);
      },
      error: function(response, status, error){
        console.log(response);
        console.log(status);
      }
    }
  )
}

function responseAction(apiResult, action){
  if (apiResult['result'] == "failed"){
    $.notify({
        icon: 'ti-na',
        message: apiResult['message']
      },{
          type: 'danger',
          timer: 4000
      });
      return;
    }
  else{
    action(apiResult);
  }
}

function LoginRequest(){
  var formUrl = "/api/v1/login";
  var postData = {
    username : $("#username").val(),
    password : $("#password").val()
  }
  apiPost(formUrl,  postData, LoginResult);
}


function GetSomething(){
  var formUrl = "/api/v1/things"
  apiGet(formUrl, ResponseExample)
}


function PostSomething(){
  var formUrl = "/api/v1/morethings";
  var postData = {
    variable1 : $("#variable1").val(),
    variable2 : $("#variable2").val(),
  }
  apiPost(formUrl, postData, ResponseExample);
}
