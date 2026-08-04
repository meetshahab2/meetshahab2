document.addEventListener('DOMContentLoaded', function () {

    // --- Fix 1: Hamburger / sidebar toggle ---
    var sidebarToggle = document.querySelector('[data-lte-toggle="sidebar"]');

    if (sidebarToggle) {
        sidebarToggle.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();

            if (window.innerWidth < 992) {
                // mobile / tablet: sidebar slides in as overlay
                document.body.classList.toggle('sidebar-open');
                document.body.classList.remove('sidebar-collapse');
            } else {
                // desktop: sidebar collapses to icons only
                document.body.classList.toggle('sidebar-collapse');
            }
        });
    }

    // Close mobile sidebar only when clicking outside of it
    document.addEventListener('click', function (e) {
        if (window.innerWidth < 992 && document.body.classList.contains('sidebar-open')) {
            var sidebar = document.querySelector('.app-sidebar');
            if (sidebar && !sidebar.contains(e.target) && !sidebarToggle.contains(e.target)) {
                document.body.classList.remove('sidebar-open');
            }
        }
    });

    // --- Fix 2: User menu dropdown (Change password / Log out) ---
    var userToggle = document.querySelector('#jazzy-navbar [data-bs-toggle="dropdown"]');

    if (userToggle && window.bootstrap) {
        var dropdown = window.bootstrap.Dropdown.getOrCreateInstance(userToggle);

        userToggle.addEventListener('click', function (e) {
            e.preventDefault();
            e.stopPropagation();
            dropdown.toggle();
        });
    }

});