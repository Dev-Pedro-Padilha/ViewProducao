from django.shortcuts import render


#Pagina Inicial do sistema
def home(request):
    return render(request,'base.html')
