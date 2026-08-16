// Progressive enhancement for quantity inputs on the product page.
document.addEventListener('DOMContentLoaded', function () {
    var qtyForm = document.querySelector('[data-qty-form]');
    if (!qtyForm) return;

    var input = qtyForm.querySelector('input[name="quantity"]');
    var decBtn = qtyForm.querySelector('[data-qty-dec]');
    var incBtn = qtyForm.querySelector('[data-qty-inc]');

    if (decBtn) {
        decBtn.addEventListener('click', function () {
            var value = Math.max(1, parseInt(input.value || '1', 10) - 1);
            input.value = value;
        });
    }
    if (incBtn) {
        incBtn.addEventListener('click', function () {
            var value = parseInt(input.value || '1', 10) + 1;
            input.value = value;
        });
    }
});
