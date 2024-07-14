$(document).ready(function () {
    $(".dropdown-toggle-custom").next(".dropdown-menu").children().on("click", function () {
        $(this).closest(".dropdown-menu").prev(".dropdown-toggle-custom").text($(this).text());
    });


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!(/^GET|HEAD|OPTIONS|TRACE$/i.test(settings.type)) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $("#searchbar").on('keyup', function (e) {
        let filterType;
        let entityType;
        let searchValue;
        if (e.key === 'Enter' || e.keyCode === 13) {
            filterType = jQuery(".dropdown-left-setting").text();
            entityType = jQuery(".dropdown-right-setting").text();
            searchValue = jQuery("#searchbar").val();
            console.log(searchValue, "searchval")
            let postData = {"filterType": filterType, "entityType": entityType, "searchValue": searchValue};
            $.ajax({
                url: 'http://localhost:8000/search/',  // Replace with your backend API endpoint
                type: 'POST',  // HTTP method
                dataType: "json",
                contentType: 'application/json',  // Type of data you are sending
                data: JSON.stringify(postData),  // Convert JavaScript object to JSON string
                success: function (response) {
                    // Handle success response
                    console.log('POST request successful');
                    console.log(response);
                },
                error: function (xhr, status, error) {
                    // Handle error response
                    console.error('POST request failed');
                    console.log(xhr.responseText);
                }
            });
        }
    });
});

