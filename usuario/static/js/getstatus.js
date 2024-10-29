// arquivo.js

// Adiciona o evento 'change' ao elemento de seleção quando o DOM é carregado
document.addEventListener('DOMContentLoaded', function() {
  const statusSelect = document.getElementById('status');
  const acessoInput = document.getElementById('acesso');

  // Verifica se os elementos estão disponíveis
  if (statusSelect && acessoInput) {
      statusSelect.addEventListener('change', filtrarLista);
  }
});

// Função para filtrar a lista e redirecionar
function filtrarLista() {
  const filtro = document.getElementById('status').value;
  const acesso = document.getElementById('acesso').value;
  const url = '/usuarios?status=' + filtro + '&acesso=' + acesso;
  window.location.href = url;
}
