
//Focusing and related actions on hovering


$(document).ready(function(){
    $('#username-bar').hover(function(){
        $('#info-bar').text('Click To Enter Username');
    },
    function(){
        $('#info-bar').text('');
    });

    $('#username-bar').click(function(){$('#info-bar').text("Enter Your Username");});
    $('#username-bar').focus();
});


$('#password-bar').hover(function(){
        $('#info-bar').text('Click To Enter Your Password');
        $('#password-bar').focus();
    },
    function(){
        $('#info-bar').text('');
    });

$('#password-bar').click(function(){$('#info-bar').text("Your Password Please!");});


$('#reset-field').hover(function(){
        $('#info-bar').text('Clicking This Will reset The Values Entered');
    },
    function(){
        $('#info-bar').text('');
});


$('#stud-login').hover(function(){
        $('#info-bar').text('Students Login');
    },
    function(){
        $('#info-bar').text('');
});


$('#prof-login').hover(function(){
        $('#info-bar').text('Only for Professors Login');
    },
    function(){
        $('#info-bar').text('');
});

$('#username-bar').keydown(function(e){if(e.keyCode == 13 ){e.preventDefault();$('#password-bar').focus();}});
$('#password-bar').keydown(function(e){if(e.keyCode ==13 ){e.preventDefault(); $('#info-bar').text('Validating User');}});
$('#stud-login').click(function(e){ e.preventDefault(); $('#info-bar').text('Validating Student');});
$('#prof-login').click(function(e){ e.preventDefault() ;$('#info-bar').text('Validating and Logging!');});






//