// Verifica os dados no console
console.log("Dados de defeitos:", defeitosDataJson);

// Transformar dados para o gráfico - localDefeitos
const testes = defeitosDataJson.map(item => item[3]);  // Local do Defeito

// Contar a frequência de cada defeito
const testesFrequencia = {};
testes.forEach(local_defeito => {
    testesFrequencia[local_defeito] = (testesFrequencia[local_defeito] || 0) + 1; // Corrigido para usar testesFrequencia
});

// Dados para o gráfico
const chartTestes = {
    labels: Object.keys(testesFrequencia),
    datasets: [{
        label: 'Frequência de Defeitos',
        data: Object.values(testesFrequencia),
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

// Configuração do gráfico com Chart.js
const ctxTestes = document.getElementById('testesChart').getContext('2d');
const testesChart = new Chart(ctxTestes, {
    type: 'bar',
    data: chartTestes,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
