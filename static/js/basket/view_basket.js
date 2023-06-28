/**
 * JavaScript for Wild Carbon project basket app view_basket.html
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function () {

    /**
     * Update quantity on click
     * Code supplied by Code Institute
     */
    /* globals $ */
    $('.update-link').click(function(e) {
        var form = $(this).prev('.update-form');
        form.submit();
    });

      /**
       * Remove item and reload on click
       * Code supplied by Code Institute
       */
      $('.remove-item').click(function(e) {
        var csrfToken = "{{ csrf_token }}";
        var itemId = $(this).attr('id').split('remove_')[1];
        var url = `/basket/remove_from_basket/${itemId}/`;
        var data = {'csrfmiddlewaretoken': csrfToken};

        $.post(url, data)
         .done(function() {
             location.reload();
         });
    }); 
});