
//Focusing and related actions on hovering


$(document).ready(function(){
    $('#username-bar').hover(function(){
        $('#info-bar').text('Click To Enter Username');
    },
    function(){
        $('#info-bar').text('Status Bar');
    });

    $('#username-bar').click(function(){$('#info-bar').text("Enter Your Username");});
    $('#username-bar').focus();
});


$('#password-bar').hover(function(){
        $('#info-bar').text('Click To Enter Your Password');
        $('#password-bar').focus();
    },
    function(){
        $('#info-bar').text('Status Bar');
    });

$('#password-bar').click(function(){$('#info-bar').text("Your Password Please!");});


$('#reset-field').hover(function(){
        $('#info-bar').text('Clicking This Will reset The Values Entered');
    },
    function(){
        $('#info-bar').text('Status Bar');
});


$('#stud-login').hover(function(){
        $('#info-bar').text('Students Login');
    },
    function(){
        $('#info-bar').text('Status Bar');
});


$('#prof-login').hover(function(){
        $('#info-bar').text('Only for Professors Login');
    },
    function(){
        $('#info-bar').text('Status Bar');
});

$('#username-bar').keydown(function(e){if(e.keyCode == 13 ){e.preventDefault();$('#password-bar').focus();}});
$('#password-bar').keydown(function(e){if(e.keyCode ==13 ){e.preventDefault(); $('#info-bar').text('Validating User');}});
$('#stud-login').click(function(e){ e.preventDefault(); $('#info-bar').text('Validating Student');});
$('#prof-login').click(function(e){ e.preventDefault() ;$('#info-bar').text('Validating and Logging!');});




$('#profsite-search').click(function(){
    $('#profsite-search').animate({width:"700px"});
});

$('#profsite-search').mouseleave(function(){$(this).animate({width:'350px'});});



$('#profsite-search').keydown(function(e){
    $(this).css("textTransform","uppercase");
    if( e.keyCode == 13){
        e.preventDefault();

        var value=$(this).val().toUpperCase();
        var linkto='/find_stud/'+value+"/";

        $.ajax({

            url:linkto,
            type :"POST",
            data : {"id":value },
            success:function(response){
                alert(response['name'])

            }
        })
    }
});



//CSRF TOken and Validation--------

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');




function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



// CSRF TOKEN ENDS --------------------