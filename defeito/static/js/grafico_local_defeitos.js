// Verifica os dados no console
console.log("Dados de defeitos:", defeitosDataJson);

// Transformar dados para o gráfico
const localDefeitos = defeitosDataJson.map(item => item[4]);  // Local do Defeito

// Contar a frequência de cada defeito
const localDefeitoFrequencia = {};
localDefeitos.forEach(local_defeito => {
    localDefeitoFrequencia[local_defeito] = (localDefeitoFrequencia[local_defeito] || 0) + 1; // Corrigido para usar localDefeitoFrequencia
});

// Dados para o gráfico
const chartData = {
    labels: Object.keys(localDefeitoFrequencia),
    datasets: [{
        label: 'Frequência de Defeitos',
        data: Object.values(localDefeitoFrequencia),
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        borderWidth: 1
    }]
};

// Configuração do gráfico com Chart.js
const ctx = document.getElementById('localDefeitosChart').getContext('2d');
const localDefeitosChart = new Chart(ctx, {
    type: 'bar',
    data: chartData,
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
