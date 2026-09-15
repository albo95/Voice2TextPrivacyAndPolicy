// Chiude il menu lingua (<details class="lang-menu">) cliccando fuori o con Esc.
(function () {
    function closeAll(except) {
        document.querySelectorAll('details.lang-menu[open]').forEach(function (d) {
            if (d !== except) d.removeAttribute('open');
        });
    }
    document.addEventListener('click', function (e) {
        var inside = e.target.closest ? e.target.closest('details.lang-menu') : null;
        closeAll(inside);
    });
    document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape') closeAll(null);
    });
})();
