//Função que envia uma requisição com o valor de status para a url:usuarios
function filtrarLista() {
    var filtro = document.getElementById('status').value;
    var acesso = document.getElementById('acesso').value;
    var url = '/usuarios?status=' + filtro + '&acesso=' + acesso;
    window.location.href = url;
  }