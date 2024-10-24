from django.urls import path
from producao import views

urlpatterns = [
    #rota, view responsavel, nome de referencia
    
    path('',views.producao_list,name='producao'),
    path('detalha/<str:codigo>/<str:nserie>',views.producao_detalha,name='producao.detalhe'),
    path('medidas/<str:codigo>/<str:nserie>', views.producao_medidas,name='producao.medidas'),
    path('perifericos/<str:codigo>/<str:nserie>', views.perifericos_cadastrados, name='producao.perifericos'),
    path('defeitos/<str:codigo>/<str:nserie>', views.defeitos, name='producao.defeitos'),

       
]