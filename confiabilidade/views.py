import requests
from django.shortcuts import render

# Create your views here.
def registros_read(request):
    #URL da API
    url = 'http://localhost:3000/registroconfiabilidade'
    
    #Fazendo a requisição para a API
    response = requests.get(url)
    
    #Verificando se a resposta foi bem-sucedida
    if response.status_code == 200:
        api_data = response.json()
    else:
        api_data = {}
        
    return render(request, 'confiabilidade.html', {'api_data': api_data})