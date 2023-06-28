/**
 * JavaScript for Wild Carbon project plants app plant_detail.html
 */

/**
 * Add functions for page manipulation on page load completion
 */
document.addEventListener('DOMContentLoaded', function () {
    /* 
    * Disable +/- buttons outside 1-99 range.
    * If no size is passed to the function, the parameter will have a value of undefined by default,
    * which prevents any errors 
    * The following quantity selector code was supplied by Code Institute
    */
    function handleEnableDisable() {

        let currentValue = parseInt($(`#id-qty`).val());
        console.log(currentValue)

        let minusDisabled = currentValue < 2;
        let plusDisabled = currentValue > 98;
         /* globals $ */
        $('#decrement-qty').prop('disabled', minusDisabled);
        $('#increment-qty').prop('disabled', plusDisabled);
    }

    // Check enable/disable every time the input is changed
    $('#qty-input').change(function() {
        handleEnableDisable();
    });

    // Increment quantity
    $('#increment-qty').click(function(e) {
        e.preventDefault();
        let currentValue = parseInt($('#id-qty').val());
        $('#id-qty').val(currentValue + 1);
        handleEnableDisable();
    });

    // Decrement quantity
    $('#decrement-qty').click(function(e) {
        e.preventDefault();
        let currentValue = parseInt($('#id-qty').val());
        $('#id-qty').val(currentValue - 1);
        handleEnableDisable();
    });

    function handleEnableDisable1() {

        let currentValue = parseInt($(`#id-qty-1`).val());
        console.log(currentValue)

        let minusDisabled = currentValue < 2;
        let plusDisabled = currentValue > 98;
         /* globals $ */
        $('#decrement-qty-1').prop('disabled', minusDisabled);
        $('#increment-qty-1').prop('disabled', plusDisabled);
    }

    // Check enable/disable every time the input is changed
    $('#qty-input-1').change(function() {
        handleEnableDisable1();
    });

    // Increment quantity
    $('#increment-qty-1').click(function(e) {
        e.preventDefault();
        let currentValue = parseInt($('#id-qty-1').val());
        $('#id-qty-1').val(currentValue + 1);
        handleEnableDisable1();
    });

    // Decrement quantity
    $('#decrement-qty-1').click(function(e) {
        e.preventDefault();
        let currentValue = parseInt($('#id-qty-1').val());
        $('#id-qty-1').val(currentValue - 1);
        handleEnableDisable1();
    });
    // End of quantity selector code supplied by Code Institute
});