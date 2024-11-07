// Obtenha o índice selecionado do input HTML
const valor = parseInt(document.getElementById('indice').value);
console.log("Valor:", valor);

// Define os dados usando JSON válido
console.log("Dados de defeitos:", defeitosDataJson);  // Verifica os dados no console

// Transformar dados para o gráfico
const defeitos = defeitosDataJson.map(item => item[valor]);  // Tipo de Defeito

// Contar a frequência de cada defeito
const defeitoFrequencia = {};
defeitos.forEach(defeito => {
    defeitoFrequencia[defeito] = (defeitoFrequencia[defeito] || 0) + 1;
});

// Dados para o gráfico
const chartDefeitos = {
    labels: Object.keys(defeitoFrequencia),
    datasets: [{
        label: 'Frequência de Defeitos',
        data: Object.values(defeitoFrequencia),
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

// Configuração do gráfico com Chart.js
const ctxDefeitos = document.getElementById('defeitosChart').getContext('2d');
const defeitosChart = new Chart(ctxDefeitos, {
    type: 'bar',
    data: chartDefeitos,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
