/**
 * Base JavaScript for Wild Carbon project
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener("DOMContentLoaded", function () {

    //Scroll back to top of page on back to top button click
    document.getElementById("back-to-top-button").addEventListener("click", function () {
        window.scroll({
            top: 0,
            left: 0,
            behavior: "smooth",
        });
    });
});
