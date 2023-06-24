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
    document.getElementById('footer-left-back-to-top').addEventListener('mouseover', addHoverEffect);
    document.getElementById('footer-right-contact').addEventListener('mouseover', addHoverEffect);
    document.getElementById('footer-right-facebook').addEventListener('mouseover', addHoverEffect);
    document.getElementById('footer-left-back-to-top').addEventListener('mouseleave', removeHoverEffect);
    document.getElementById('footer-right-contact').addEventListener('mouseleave', removeHoverEffect);
    document.getElementById('footer-right-facebook').addEventListener('mouseleave', removeHoverEffect);
});

/**
 * Add hover effects to buttons on mouse enter
 */
function addHoverEffect() {
    this.style.border = '3px solid var(--button-background)';
}

/**
 * Remove hover effects from buttons on mouse leave
 */
function removeHoverEffect() {
    this.style.border = 'none';
}
