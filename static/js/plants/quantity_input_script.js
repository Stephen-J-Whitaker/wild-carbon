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
    function handleEnableDisable(itemId, size) {
        let currentValue;
        if (size) {
            currentValue = parseInt($(`.size_${itemId}_${size}`).val());
        } else {
            currentValue = parseInt($(`.id_qty_${itemId}`).val());
        }

        let minusDisabled = currentValue < 2;
        let plusDisabled = currentValue > 98;
         /* globals $ */
        if (size) {
            $(`.decrement-size_${itemId}_${size}`).prop('disabled', minusDisabled);
            $(`.increment-size_${itemId}_${size}`).prop('disabled', plusDisabled);
        } else {
            $(`.decrement-qty_${itemId}`).prop('disabled', minusDisabled);
            $(`.increment-qty_${itemId}`).prop('disabled', plusDisabled);
        }
    }

    // Ensure proper enabling/disabling of all inputs on page load
    let allQtyInputs = $('.qty_input');
    for(var i = 0; i < allQtyInputs.length; i++){
        let itemId = $(allQtyInputs[i]).data('item_id');
        let size = $(allQtyInputs[i]).data('size');
        handleEnableDisable(itemId, size);
    }

    // Check enable/disable every time the input is changed
    $('.qty_input').change(function() {
        let itemId = $(this).data('item_id');
        let size = $(this).data('size');
        handleEnableDisable(itemId, size);
    });

    // Increment quantity
    $('.increment-qty').click(function(e) {
        let allQuantityInputs;
        e.preventDefault();
        let itemId = $(this).data('item_id');
        let size = $(this).data('size');
        let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        if (size) {
            allQuantityInputs = $(`.input-group-${itemId} input[data-size='${size}']`);
        } else {
            allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
        }
        let currentValue = parseInt($(closestInput).val());
        $(allQuantityInputs).val(currentValue + 1);
        handleEnableDisable(itemId, size);
    });

    // Decrement quantity
    $('.decrement-qty').click(function(e) {
        let allQuantityInputs = 0; 
        e.preventDefault();
        let itemId = $(this).data('item_id');
        let size = $(this).data('size');
        let closestInput = $(this).closest('.input-group').find('.qty_input')[0];
        if (size) {
            allQuantityInputs = $(`.input-group-${itemId} input[data-size='${size}']`);
        } else {
            allQuantityInputs = $(`.input-group-${itemId} input[name='quantity']`);
        }
        let currentValue = parseInt($(closestInput).val());
        $(allQuantityInputs).val(currentValue - 1);
        handleEnableDisable(itemId, size);
    });
    // End of quantity selector code supplied by Code Institute
});