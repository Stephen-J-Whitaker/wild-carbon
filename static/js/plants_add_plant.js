/**
 * JavaScript for Wild Carbon project plants app add_plant.html
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function () {

    /**
     * Update image filename notification text supplied by Code Institute
     */
    $('#new-image').change(function() {
        var file = $('#new-image')[0].files[0];
        $('#filename').text(`Image will be set to: ${file.name}`);
    });
});
