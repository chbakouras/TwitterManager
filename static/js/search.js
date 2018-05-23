function loadNextPageTweets() {
    var search = $(".search-val").last().val();
    var maxId = $(".max-id-val").last().val();
    return $.ajax({
        type: "POST",
        url: "/twitter-search-live-load/",
        data: {
            'search': search,
            'max_id': maxId
        },
        success: function (response) {
            document.getElementById("tweets").innerHTML = document.getElementById("tweets").innerHTML + response;
        }
    })
}

function retweet(twitterTweetId) {
    return $.ajax({
        type: "POST",
        url: "/retweet/" + twitterTweetId + "/",
        success: function (response) {
            console.log(response);
        }
    });
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
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

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
