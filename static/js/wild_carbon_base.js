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

    // Hover effects for buttons and links
    document.getElementById('footer-left-back-to-top').addEventListener('mouseover', addHoverEffect);
    document.getElementById('footer-right-contact').addEventListener('mouseover', addHoverEffect);
    document.getElementById('footer-right-facebook').addEventListener('mouseover', addHoverEffect);
    document.getElementById('privacy-policy-link').addEventListener('mouseover', addLinkHoverEffect);
    
    document.getElementById('footer-left-back-to-top').addEventListener('mouseleave', removeHoverEffect);
    document.getElementById('footer-right-contact').addEventListener('mouseleave', removeHoverEffect);
    document.getElementById('footer-right-facebook').addEventListener('mouseleave', removeHoverEffect);
    document.getElementById('privacy-policy-link').addEventListener('mouseleave', removeLinkHoverEffect);

    // Show contact us modal when button pressed
    document.getElementById("contact-us-button").addEventListener("click", function () {
        document.getElementsByTagName('body')[0].style.position = 'fixed';
        document.getElementById('contact-us-modal').classList.toggle('display-none');
    });

    // Close contact us modal when button pressed
    document.getElementById("contact-us-close-button").addEventListener("click", function () {
        document.getElementsByTagName('body')[0].style.position = '';
        document.getElementById('contact-us-modal').classList.toggle('display-none');
    });

    // Show privacy policy modal when button pressed
    document.getElementById("privacy-policy-link").addEventListener("click", function () {
        document.getElementsByTagName('body')[0].style.position = 'fixed';
        document.getElementById('privacy-policy-modal').classList.toggle('display-none');
    });

    // Close privacy policy modal when button pressed
    document.getElementById("privacy-policy-close-button").addEventListener("click", function () {
        document.getElementsByTagName('body')[0].style.position = '';
        document.getElementById('privacy-policy-modal').classList.toggle('display-none');
    });
});

/**
 * Add hover effects to button on mouse enter
 */
function addHoverEffect() {
    this.style.border = '3px solid var(--button-background)';
}

/**
 * Remove hover effects from button on mouse leave
 */
function removeHoverEffect() {
    this.style.border = 'none';
}

/**
 * Add hover effects to link on mouse enter
 */
function addLinkHoverEffect() {
    this.style.textDecoration = 'underline';
}

/**
 * Remove hover effects from link on mouse leave
 */
function removeLinkHoverEffect() {
    this.style.textDecoration = 'none';
}
