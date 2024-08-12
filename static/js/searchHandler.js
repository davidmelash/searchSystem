$(document).ready(function () {
    $(".dropdown-toggle-custom").next(".dropdown-menu").children().on("click", function () {
        $(this).closest(".dropdown-menu").prev(".dropdown-toggle-custom").text($(this).text());
    });

    $(".searchbar-text-input").click(function () {

        jQuery("#searchbar").val("");
        jQuery("#datePicker").attr("id", "datePicker-block");
    });

    function renderProfiles(data) {
        jQuery(".card-setting").empty();
        for (let profile of data) {
            let full_name = profile.full_name
            let phone_number = profile.phone_number
            let data_of_birth = profile.data_of_birth
            let address = profile.address
            let identification_number = profile.identification_number
            let comments = profile.comments
            let profile_pic = profile.profile_pic
            profile_pic = profile.profile_pic ? `/media/${profile_pic}`: "/static/images/user_icon.png"
            let profile_id = profile.id
            let render_text = `
            <a href="/profile/${profile_id}" class="reset-link-style">
            <div class="card mb-3">
        <div class="row g-0">
            <div class="col-md-2">
                <img src=${profile_pic} class="img-fluid rounded-start" alt="Profile image" style="height: 100% !important;">
            </div>
            <div class="col">
                <div class="card-body" style="height: 163px;">
                    <div class="row mt-1">
                        <div class="col-md-auto">
                            <span class="col card-item">${full_name}</span>
                        </div>
                        <div class="col-md-auto">
                            <span class="col card-item">${phone_number}</span>
                        </div>
                        <div class="col-md-auto">
                            <span class="col card-item">${data_of_birth}</span>
                        </div>

                    </div>
                    <div class="row" style="    margin-top: 18px;">
                        <div class="col-md-auto " style="max-width: 550px;">
                            <div class="card-item ">
                            <div class="col single-line">${address}</div>
                            </div>
                        </div>
                        <div class="col-md-auto ">
                            <div class="col card-item">ІПН ${identification_number}</div>
                        </div>


                    </div>
                    <div class="row  card-item-comment">
                        <div class="col single-line">
                            <span class=" single-line">${comments}</span>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
    </a>
`;
            jQuery(".card-setting").append(render_text);
        }

    }


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
                url: 'http://localhost:9000/search/',  // Replace with your backend API endpoint
                type: 'POST',  // HTTP method
                dataType: "json",
                contentType: 'application/json',  // Type of data you are sending
                data: JSON.stringify(postData),  // Convert JavaScript object to JSON string
                success: function (response) {
                    // Handle success response
                    renderProfiles(response)
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

