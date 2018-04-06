var view = 'list';
var gridButton;
var listButton;

$(document).ready(function () {
    startJobPolling();

    $(".auto-update").change(liveSearch);

    gridButton = $('#grid-button');
    listButton = $('#list-button');
});

function unFollow(id) {
    $.post("/un-follow/" + id + "/")
        .done(function (data) {
            $("#" + id).hide();
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

function synchronize() {
    $.post("/synchronize/")
        .done(function (data) {
            startJobPolling()
        })
        .fail(function (data) {
            $('<div class="alert alert-danger fade in"><a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a> <strong>Failed! ' + data.responseText + '</strong></div>').appendTo("body");
        });
}

function startJobPolling() {
    $.get("/jobs/")
        .done(function (data) {
            if (data.length > 0) {
                liveSearch()
                    .success(function (res) {
                        $('#list-table').DataTable({searching: false});
                    });

                $('#synchronize-cog').html('<i class="fa fa-refresh fa-spin" aria-hidden="true"></i>')
                setTimeout(startJobPolling, 3000)
            } else {
                $('#synchronize-cog').html('<i class="fa fa-refresh" aria-hidden="true"></i>')
            }
        })
}

var liveSearch = function () {
    var search = $('#search').val();
    var friendship = $('#friendship').val();

    return $.ajax({
        type: "POST",
        url: "/live-search/",
        data: {
            'search': search,
            'friendship': friendship,
            'view': view
        },
        success: function (response) {
            document.getElementById("friends").innerHTML = response;
        }
    })
}

function massUnfollow() {
    $('.friend').each(function (index, friend) {
        var id = $(friend).data('id')
        if (id !== null) {
            unFollow(id)
        }
    })
}

var timer;

function up() {
    timer = setTimeout(liveSearch, 500);
}

function down() {
    clearTimeout(timer);
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

function listLayout() {
    gridButton.removeClass("active");
    listButton.addClass("active");
    view = 'list';
    liveSearch()
        .success(function (res) {
            $('#list-table').DataTable({searching: false});
        });
}

function gridLayout() {
    listButton.removeClass("active");
    gridButton.addClass("active");
    view = 'grid';
    liveSearch();
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
