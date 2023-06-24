/**
 * Base JavaScript for Wild Carbon project
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function () {

    // Scroll back to top of page on back to top button click
    document.getElementById('back-to-top-button').addEventListener('click', function () {
        window.scroll({
            top: 0,
            left: 0,
            behavior: 'smooth',
        });
    });

    // Remove hover effect from buttons that remain after click
    document.getElementById('footer-left-back-to-top').addEventListener('click', removeHoverEffect);
    document.getElementById('footer-right-contact').addEventListener('click', removeHoverEffect);
    document.getElementById('footer-right-facebook').addEventListener('click', removeHoverEffect);
});

/**
 * Remove hover effects from buttons after click
 */
function removeHoverEffect() {
    this.style.border = 'none';
}
