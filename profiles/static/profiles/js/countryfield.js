/**
 * JavaScript for Wild Carbon project profile app profile.html
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function() {

    /**
     * Change coutry field style dependent on whether selected
     * Code supplied by Code Institute
     */
    /* globals $ */
    let countrySelected = $('#id_default_country').val();
    if (!countrySelected) {
        $('#id_default_country').css('color', '#aab7c4');
    }
    $('#id_default_country').change(function () {
        countrySelected = $(this).val();
        if (!countrySelected) {
            $(this).css('color', '#aab7c4');
        } else {
            $(this).css('color', '#000');
        }
    });
    // End of code supplied by Code Institute

});