from django.urls import path
from login import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('',views.login_view,name='login'),
    path('logout/', views.logout, name='logout'),
]