from django.urls import path
from produto import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('',views.produto_list,name='produto'),
    path('produto_insert', views.produto_insert,name='produto.insert'),
    path('produto_delete/<cd_produto>', views.produto_delete,name='produto.delete'),
    path('produto_update/<cd_produto>', views.produto_update,name='produto.update')
       
]