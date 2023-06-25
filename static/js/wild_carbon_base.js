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

    // Show contact us modal when button pressed
    document.getElementById("contact-us-button").addEventListener("click", function () {
        //Make button look pressed down by styling border
        document.getElementsByTagName('body')[0].style.position = 'fixed';

        document.getElementById('contact-us-modal').classList.toggle('display-none');
        // windowHeight = document.getElementsByTagName('body')[0].scrollHeight;
        // console.log(windowHeight);
        // window.scrollTo(0, windowHeight);
        // document.getElementById('contact-us-modal').style.position = 'fixed';
    });

    // Close contact us modal when button pressed
    document.getElementById("contact-us-close-button").addEventListener("click", function () {
        //Make button look pressed down by styling border
        this.classList.toggle('button-press');
        document.getElementsByTagName('body')[0].style.position = 'fixed';

        setTimeout(function () { topTenButton.classList.toggle('button-press'); }, 200);
        document.getElementById('contact-us-modal').classList.toggle('display-none');
    });
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
