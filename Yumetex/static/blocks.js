$(document).ready(function () {
    console.log("functioning!");

    $("#submit-button").click(function () {
        let searchQuery = $("#search-box").val().trim();
        console.log(searchQuery);

        // go to search results page, ie render the search_results.html template
        // do we need to ajax for this?

        if (searchQuery) {
            // Redirect to search_results.html with query parameter searchQuery
            window.location.href = "/search_results?query=" + encodeURIComponent(searchQuery);
        }

        $("#search-box").val('').focus();
    })

    $("#search-box").on("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            $("#submit-button").click();
        }
    })

    // Add data
    $(document).on("click", "#submit-add-button", function () {
        console.log("Submitting a new entry to server...");

        let itemname = $("#itemname").val().trim();
        let articleNo = $("#articleNo").val().trim();
        let price = $("#price").val().trim();
        let MOQ = $("#MOQ").val().trim();
        let fabricComp = $("#fabricComp").val().trim();
        let description = $("#description").val().trim();
        let fabricImage = $("#fabricImage").val().trim();

        let fields = [
            { id:"#itemname" , message: "*Please enter an article name."},
            { id: "#articleNo", message: "*Please enter an article number." },
            { id: "#price", message: "*Please enter a valid price." },
            { id: "#MOQ", message: "*Please enter the minimum order quantity." },
            { id: "#fabricComp", message: "*Please enter fabric composition." },
            { id: "#description", message: "*Please enter a description." },
            { id: "#fabricImage", message: "*Please enter an image link." }
        ];

        $(".error-message").remove();
        $("[id]").removeClass("error-border");

        let errorField = null;

        // Loop through each field to check if it's empty and apply error styles/messages
        fields.forEach(function (field) {
            let value = $(field.id).val().trim();

            if (!value) {
                errorField = field.id;
                $(field.id).addClass("error-border")
                    .after('<div class="error-message">' + field.message + '</div>');
            }
        });

        if (price && isNaN(price)) {
            errorField = "#price";
            $("#price").addClass("error-border")
                .after('<div class="error-message">*Please enter a valid price (numeric value).</div>');
        }
        
        if (MOQ && isNaN(MOQ)) {
            errorField = "#MOQ";
            $("#MOQ").addClass("error-border")
                .after('<div class="error-message">*Please enter a valid minimum order quantity (numeric value).</div>');
        }

        if (errorField) {
            $(errorField).focus();
            return;
        }

        // TODO: add Enter event to go to next text box, and submit


        // AJAX request to send the data to the server
        $.ajax({
            type: "POST",
            url: "/add", // Adjust the URL to match your route
            data: {
                itemname: itemname,
                articleNo: articleNo,
                price: price,
                MOQ: MOQ,
                fabricComp: fabricComp,
                description: description,
                fabricImage: fabricImage
            },
            success: function (response) {
                // Handle success (clear fields, show success message)
                $('#success-message-container').html(`
                <div class=" success-message">
                    New item successfully added! <a id="success-see-it-here" href="/view/${response.item.id}" >See it here.</a>
                </div>
            `);

                // Clear input fields and focus on the first input
                $("[id]").val('');
                $("#articleNo").focus();
            },
            error: function (xhr, status, error) {
                // Handle error (show error message)
                let errorMessage = xhr.responseJSON.error || "An error occurred. Please try again.";
                $('#success-message-container').html(`
                <div class="alert alert-danger">${errorMessage}</div>
            `);
            }
        });

        // setTimeout(function () {
        //     $(".success-message").fadeOut();
        // }, 3000); // 3 seconds
    });

    // Display favorite blocks
    fav_blocks.forEach(block => {
        let blockHTML = `
            <div class="featured-item col-lg-3 col-sm-12">
                <a href="/view/${block.id}">
                    <img src="${block.image}" alt="${block.name}" class="home-page-images">
                    <p class="block-name">${block.name}</p>
                </a>
            </div>
        `;
        $("#featured-container").append(blockHTML);
    });

})