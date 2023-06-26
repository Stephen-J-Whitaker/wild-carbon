/**
 * JavaScript for Wild Carbon project plants app add_plant.html
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function () {

    /**
     * Use ajax to check if plant common name input entry is unique for the user
     * Code taken from music aid project:
     * https://github.com/Stephen-J-Whitaker/music-aid/blob/main/static/js/songbook_js/songbook_song_add_edit.js
     */
    // Actions to be taken on completion of form page load
    let originalCommonName = $('#id_common_name').val();

    let commonName = $('#id_common_name').val();
    let trimmedCommonName = commonName.trim();
    let commonNameLabel = document.querySelector('label[for="id_common_name"]');
    $('#id_common_name').val(trimmedCommonName);

    // End of actions to be taken on completion of form page load

    function validateUnique() {
        if ($('#id_common_name').val() != '') {
            /* globals $ */
            commonName = $('#id_common_name').val();
            // Replace regex for multi white space removal sourced at:
            // https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php
            trimmedCommonName = commonName.trimStart().replace(/  +/g, ' ');
            commonName = trimmedCommonName.trimEnd();
            // Ajax code adapted from code found at this site:
            // https://www.geeksforgeeks.org/handling-ajax-request-in-django/
            $.ajax(
            {
                type:'GET',
                url: '/common_name_validate',
                data:{
                    common_name: commonName
                },
                success: function(data) {
                    if (data === 'in_use') {
                        if ($('#id_common_name').val().trimStart().trimEnd().replace(/  +/g, ' ') === originalCommonName) {
                            $('#id_common_name').css('background-color', 'white');
                            commonNameLabel.classList.remove('common-name-status');
                            $('#plant-submit-btn').show();
                        } else {
                            $('#id_common_name').css('background-color', 'rgb(255, 137, 137)');
                            commonNameLabel.classList.add('common-name-status');
                            $('#plant-submit-btn').hide();
                        }
                    } else {
                        $('#id_common_name').css('background-color', 'white');
                        commonNameLabel.classList.remove('common-name-status');
                        $('#plant-submit-btn').show();
                    }
                }
            });
            // End of ajax code from https://www.geeksforgeeks.org/handling-ajax-request-in-django/
        }
    }

    /**
     * Switch off submit event listener and submit form
     */
    function submitForm() {
        if ($('#plant-submit-btn').is(':visible')) {
            $('form').off('submit');
            $('form').submit();
        }
    }
    
    validateUnique();
    $('#id_common_name').keyup('input', validateUnique);
    $('#id_common_name').change(validateUnique);

    /**
     * Trim any trailing white spaces before revalidation
     * and submit form only if save button has not been removed by
     * validation
     */
    $('form').submit(function(thisEvent) {

        thisEvent.preventDefault();
        commonName = $('#id_common_name').val();
        trimmedCommonName = commonName.trimEnd();
        // Replace regex for multi white space removal sourced at:
        // https://www.tutorialrepublic.com/faq/how-to-replace-multiple-spaces-with-single-space-in-javascript.php
        trimmedCommonName = trimmedCommonName.replace(/  +/g, ' ');
        $('#id_common_name').val(trimmedCommonName);
        setTimeout(validateUnique, 100);

        setTimeout(submitForm, 300);
    });
    // End of code taken from music aid project

    /**
     * Update image filename notification text supplied by Code Institute
     */
    $('#new-image').change(function() {
        var file = $('#new-image')[0].files[0];
        $('#filename').text(`Image will be set to: ${file.name}`);
    });
});
