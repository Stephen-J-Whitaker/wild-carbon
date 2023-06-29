/**
 * JavaScript for Wild Carbon project basket app view_basket.html
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function () {
    /**
     * Remove item and reload on click
     * Code supplied by Code Institute
     */
    $('.remove-item').click(function(e) {
        /* globals $ */
        let csrfToken = $(this).data('csrf_token');
        let itemId = $(this).attr('id').split('remove_')[1];
        let url = `/remove_from_basket/${itemId}/`;
        let data = {'csrfmiddlewaretoken': csrfToken};

        $.post(url, data)
        .done(function() {location.reload();});
    }); 
});