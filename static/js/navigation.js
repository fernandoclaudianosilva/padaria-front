// Mobile menu + search toggle
document.addEventListener('DOMContentLoaded', function () {
    var menuToggle = document.querySelector('[data-menu-toggle]');
    var mobileNav = document.querySelector('[data-mobile-nav]');
    var mobileNavClose = document.querySelector('[data-mobile-nav-close]');
    var searchToggle = document.querySelector('[data-search-toggle]');
    var searchBar = document.querySelector('[data-search-bar]');

    if (menuToggle && mobileNav) {
        menuToggle.addEventListener('click', function () {
            mobileNav.classList.add('is-open');
            document.body.style.overflow = 'hidden';
        });
    }
    if (mobileNavClose && mobileNav) {
        mobileNavClose.addEventListener('click', function () {
            mobileNav.classList.remove('is-open');
            document.body.style.overflow = '';
        });
    }
    if (searchToggle && searchBar) {
        searchToggle.addEventListener('click', function (e) {
            e.preventDefault();
            searchBar.classList.toggle('is-open');
            if (searchBar.classList.contains('is-open')) {
                var input = searchBar.querySelector('input');
                if (input) input.focus();
            }
        });
    }

    // Highlight active nav link
    var links = document.querySelectorAll('.main-nav a, .mobile-nav a');
    links.forEach(function (link) {
        if (link.getAttribute('href') === window.location.pathname) {
            link.classList.add('is-active');
        }
    });
});
