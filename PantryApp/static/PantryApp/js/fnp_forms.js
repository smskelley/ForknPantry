$(document).ready(function(){
    var minPassLen = 5;
    var invalidPasswords = function(pass1, pass2) {
        if (pass1 != pass2) {
            return "Passwords don't match";
        }
        if (pass1.length < minPassLen) {
            return "Password is too short";
        }
        return false;
    };
    var addFormErrorMsg = function(msg,loc) {
        $("<p class=\"form_error\">" + msg + "</p>").insertAfter(loc);
    };

    $('#login').click(function(event){
        // clean the slate each time
        $('.form_error').remove();

        if ($('#username').val().length < 3) {
            event.preventDefault();
            addFormErrorMsg("Username is too short", '#username');
        }
        
        if ($('#pass').val().length < minPassLen) {
            // notify user the passwords don't match, prevent from posting
            event.preventDefault();
            addFormErrorMsg("Password is too short", '#pass');
        }
        if (!$('.form_error').length) {
            // if we've gotten this far and there's no error messages, the form
            // is likely valid, so post it.
            console.log("valid form.");
        }
    });

    $('#register').click(function(event){
        // clean the slate each time
        $('.form_error').remove();
        
        var error;
        if (error = invalidPasswords($('#pass1').val(), $('#pass2').val())) {
            // notify user the passwords don't match and prevent from posting
            event.preventDefault();
            addFormErrorMsg(error, '#pass2');
        }
        if ($('#username').val().length < 3) {
            event.preventDefault();
            addFormErrorMsg("Username is too short", '#username');
        }
        if (!$('.form_error').length) {
            // if we've gotten this far and there's no error messages, the form
            // is likely valid, so post it.
            console.log("valid form.");
        }
    });
});
