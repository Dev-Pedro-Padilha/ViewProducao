from django.shortcuts import render, redirect
import requests

def login_view(request):
    api_data = {}  # Inicialize api_data como um dicionário vazio
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")

        # URL da API
        url = 'http://localhost:3000/auth/login'

        # Dados JSON a serem enviados para a API
        data = {
            "username": username,
            "password": password
        }

        # Fazendo a requisição para a API
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()  # Lança um erro para status de resposta ruim
            print(response)
            # Verificando se a resposta foi bem-sucedida
            if response.status_code == 201:
                api_data = response.json()
                request.session['token'] = api_data.get('token')
                request.session['username'] = username
                request.session['message'] = api_data.get('message')
                request.session['name'] = api_data.get('user')['cn']
                request.session['title'] = api_data.get('user')['title']
                request.session['department'] = api_data.get('user')['department']
                request.session['mail'] = api_data.get('user')['mail']
                photo = api_data.get('user')['thumbnailPhoto']
                request.session['photo'] = f"data:image/png;base64,{photo}"

                # Redirecionar para a página 'home' em caso de sucesso
                return redirect('home')
            else:
                # Captura erro caso credenciais sejam inválidas ou API retorne erro
                api_data['error'] = "Credenciais inválidas ou erro no servidor"

        except requests.exceptions.RequestException:
            # Captura erros de conexão com a API
            api_data['error'] = "Erro de conexão com o servidor. Tente novamente."

    # Renderizar template de login com mensagem de erro, se houver
    return render(request, 'login.html', {'error': api_data.get('error')})

def logout(request):
    request.session.flush()  # Limpa todos os dados da sessão
    return redirect('login')
