document.getElementById("downloadExcel").addEventListener("click", function() {
    window.location.href = "{% url 'producao.detalhe' codigo nserie %}?download=1";
});

document.getElementById("scrollToBottom").addEventListener("click", function() {
    window.scrollTo(0, document.body.scrollHeight);
});

