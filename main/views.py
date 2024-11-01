from django.shortcuts import render
from login.decorators import login_required  # Importa o decorator


#Pagina Inicial do sistema
@login_required  # Aplica o decorator aqui
def home(request):
    print("chamando home")
    return render(request,'base.html')
