/**
 * Search and sort JavaScript for Wild Carbon project plant lists
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function () {

    /**
     * Reload the plant listing page with plants ordered as per the ordering selector box
     * Sort search js supplied by Code Institute
     */
     /* globals $ */
    $('#sort-selector').change(function() {
        const selector = $(this);
        let currentUrl = new URL(window.location);

        let selectedVal = selector.val();
        if(selectedVal != 'reset'){
            let sort = selectedVal.split('__')[0];
            let direction = selectedVal.split('__')[1];

            currentUrl.searchParams.set('sort', sort);
            currentUrl.searchParams.set('direction', direction);

            window.location.replace(currentUrl);
        } else {
            currentUrl.searchParams.delete('sort');
            currentUrl.searchParams.delete('direction');

            window.location.replace(currentUrl);
        }
    });
    //End of sort search js code supplied by Code Institute

    // Code to go to previous position on page refresh adapted from
    //https://css-tricks.com/memorize-scroll-position-across-page-loads/
    window.addEventListener('beforeunload', () => {
    localStorage.setItem('sidebar-scroll', window.scrollY);
    });

    let top = localStorage.getItem('sidebar-scroll');
    if (top !== null) {
        window.scroll({
            top: top,
            left: 0,
            behavior: 'smooth',
        });
    }
    //End of code from https://css-tricks.com/memorize-scroll-position-across-page-loads/

});