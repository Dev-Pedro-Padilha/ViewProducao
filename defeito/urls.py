from django.urls import path
from defeito import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('',views.defeitos,name='defeito'),      
]