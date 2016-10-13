function unFollow(id) {
    $.post("/un-follow/" + id + "/")
        .done(function (data) {
            $("#" + id + " > .actions > .un-follow").hide();
            $("#" + id + " > .actions > .follow").show();
        })
        .fail(function (data) {
            console.log(data);
            $('<div class="alert alert-danger fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a> <strong>Failed! ' + data.responseText + '</strong></div>').appendTo("body");
        });
}

function follow(id) {
    $.post("/follow/" + id + "/")
        .done(function (data) {
            $("#" + id + " > .actions > .un-follow").show();
            $("#" + id + " > .actions > .follow").hide();
        })
        .fail(function (data) {
            $('<div class="alert alert-danger fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a> <strong>Failed! ' + data.responseText + '</strong></div>').appendTo("body");
        });
}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});