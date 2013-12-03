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
    var validEmail = function(email) {
        if (!email) {
            return false;
        }
        try {
            email.split("@")[1].split(".").length;
        } catch (err) {
            return false;
        }
        return true;
    };
    var addFormErrorMsg = function(msg,loc) {
        $("<p class=\"form_error\">" + msg + "</p>").insertAfter(loc);
    };

    $('#login').click(function(event){
        // clean the slate each time
        $('.form_error').remove();
        
        if ($('#pass').val().length < minPassLen) {
            // notify user the passwords don't match, prevent from posting
            event.preventDefault();
            addFormErrorMsg("Password is too short", '#pass');
        }
        if (!validEmail($('#email').val())) {
            // notify user the email is invalid, prevent from posting
            event.preventDefault();
            addFormErrorMsg("Invalid email address", '#email');
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
        if (!validEmail($('#email').val())) {
            // notify user the email is invalid and prevent from posting
            event.preventDefault();
            addFormErrorMsg("Invalid email address", '#email');
        }
        if (!$('.form_error').length) {
            // if we've gotten this far and there's no error messages, the form
            // is likely valid, so post it.
            console.log("valid form.");
        }
    });
});
