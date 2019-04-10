function load_eda()
{
    console.log("function: load_eda");
    var form = document.getElementById("load_eda_form");
    form.submit();
}

function load_case_eval()
{
    console.log("function: load_case_eval");
    var form = document.getElementById("load_case_eval_form");
    form.submit();
}

function load_dynamic_prediction()
{
    console.log("function: load_dynamic_prediction");
    var form = document.getElementById("load_dynamic_prediction_form");
    form.submit();
}

function logout()
{
    console.log("function: logout");
    var form = document.getElementById("logout_form");
    form.submit();
}

$(document).ready(function(){
  $('[data-toggle="tooltip"]').tooltip();   
});