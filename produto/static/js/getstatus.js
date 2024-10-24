//Função que envia uma requisição com o valor de status para a url:usuarios
function filtrarLista() {
    var filtro = document.getElementById('controlseqprod').value;
    var ativo = document.getElementById('ativo').value;
    var jiga = document.getElementById('jiga').value;
    var url = '/produto?controlseqprod=' + filtro + '&ativo=' + ativo + '&jiga=' + jiga;
    window.location.href = url;
  }
    function handleClick() {
        alert('Ícone clicado!');
        // Ou redirecione para outra página
        // window.location.href = 'https://www.exemplo.com';
    }