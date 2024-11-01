from django.http import HttpResponseRedirect
from django.urls import reverse

def login_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.session.get('message') != 'Login successful!':  # Verifica se o usuário está autenticado
            print("Usuário não autenticado, redirecionando para a página de login.")
            return HttpResponseRedirect(reverse('login'))
        print("Usuario autenticado")
        return view_func(request, *args, **kwargs)
    return _wrapped_view
