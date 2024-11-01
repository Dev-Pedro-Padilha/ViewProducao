from django.shortcuts import render, redirect
import requests

def login_view(request):
    # Inicialize api_data como um dicionário vazio
    api_data = {}
    if request.method == 'GET':
        return render(request, 'login.html')
        
    if request.method == 'POST':
        
        username = request.POST.get("username")
        password = request.POST.get("password")
            
        #URL da API
        url = 'http://localhost:3000/auth/login'
        
        # Dados JSON a serem enviados para a API
        data = {
            "username": username,
            "password": password
        }
        
        #Fazendo a requisição para a API
        response = requests.post(url, json=data)
        # Verificando se a resposta foi bem-sucedida
        if response.status_code == 201:
            api_data = response.json()
            #print(api_data)
            # Armazenar token ou dados de autenticação na sessão
            request.session['token'] = api_data.get('token')
            request.session['username'] = username
            request.session['message'] = api_data.get('message')
            request.session['name'] = api_data.get('user')['cn']
            request.session['title'] = api_data.get('user')['title']
            request.session['department'] = api_data.get('user')['department']
            request.session['mail'] = api_data.get('user')['mail']
            
            # Aqui você pode redirecionar ou passar os dados da resposta para o contexto
            return redirect('home')
        else:
            api_data = {"error": "Invalid credentials or server error"}
    else:
        api_data = {}

    return render(request, 'login.html', {'error': api_data.get("error")})

def logout(request):
    request.session.flush()  # Limpa todos os dados da sessão
    return redirect('login')
