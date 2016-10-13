/**
 * Created by Natalay on 12/10/16.
 */

var $ = require('jquery');

$('.profile .actualizar').on("click", function(){
    var formData = new FormData($('.form-profile')[0]);
    formData.append('info',$('.form-profile textarea').text().trim());


    // using jQuery
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = $.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
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
    // realiza la peticion ajax
    $.ajax({
        type: "POST",
        url: $('.form-profile .usuario').val()+"/updateUser",
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        data: formData,
        contentType: false,
        processData: false,
        success: function(data){

            console.log(data);
        },
        error : function(err){
            console.log(err);
        }
    });

});

$('.form-profile').on("submit",function(evt){
    evt.preventDefault();
});
