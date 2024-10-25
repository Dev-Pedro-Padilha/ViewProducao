from django.urls import path, include
from main import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    path('',views.home,name='home'),
    path('usuarios', include('usuario.urls'),name='usuarios'),
    path('produto', include('produto.urls'),name='produto'),
    path('producao', include('producao.urls'),name='producao'),
    path('defeito', include('defeito.urls'),name='defeito'),
       
]


#path('', include('main.urls'))