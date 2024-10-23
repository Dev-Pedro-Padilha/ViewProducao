document.getElementById("downloadExcel").addEventListener("click", function() {
    window.location.href = "/producao?download=1";
});

document.addEventListener('DOMContentLoaded', function() {
    var rows = document.querySelectorAll('.clickable-row');
    rows.forEach(function(row) {
        row.addEventListener('click', function() {
            var href = row.getAttribute('data-href');
            window.open(href, '_blank');
        });
    });
});
