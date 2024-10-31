from django.urls import path
from confiabilidade import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('',views.registros_read,name='confiabilidade'),
    path('',views.registros_read,name='confiabilidade'),
    
]