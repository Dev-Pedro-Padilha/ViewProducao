from django.urls import path
from usuario import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('',views.usuarios_list,name='usuarios'),
    path('usuarios_insert', views.usuarios_insert,name='usuarios.insert'),
    path('usuarios_delete/<int:matricula>', views.usuarios_delete,name='usuarios.delete'),
    path('usuarios_update/<int:matricula>', views.usuarios_update,name='usuarios.update')
       
]