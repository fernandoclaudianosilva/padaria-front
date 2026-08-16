// Debounced live hint (no external requests — just UX polish for the search bar).
document.addEventListener('DOMContentLoaded', function () {
    var searchInput = document.querySelector('[data-search-input]');
    if (!searchInput) return;
    searchInput.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') {
            var bar = document.querySelector('[data-search-bar]');
            if (bar) bar.classList.remove('is-open');
        }
    });
});
