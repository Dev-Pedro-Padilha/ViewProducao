from django.shortcuts import render
from main.models import  Resultados,  Testes,  DefeitoResultados2, LocalDefeito, Defeito, Testes
from django.http import HttpResponse
from datetime import datetime
import pandas as pd
import tempfile
import json
from login.decorators import login_required  # Importa o decorator

def retornaIndicesByDate(inicio_data_hora, fim_data_hora):
    #print("retornaIndicesByDate")
    # Execute a consulta usando o ORM do Django
    # Lista de valores de NRO_SERIE a serem excluídos
    nro_serie_excluidos = list(range(11))
    indices = Resultados.objects.filter(
        dataini__range=(inicio_data_hora, fim_data_hora)).exclude(serie__in=nro_serie_excluidos).values('indice', 'magnus', 'serie').order_by('serie')

    return indices

def retornaIndicesByCodigo(inicio_data_hora, fim_data_hora, codigo):
    #print("retornaIndicesByCodigo")
    # Execute a consulta usando o ORM do Django
    # Lista de valores de NRO_SERIE a serem excluídos
    nro_serie_excluidos = list(range(11))
    indices = Resultados.objects.filter(
        dataini__range=(inicio_data_hora, fim_data_hora), magnus=codigo).exclude(serie__in=nro_serie_excluidos).values('indice', 'magnus', 'serie').order_by('serie')

    return indices

def GetDataDefeitos(indices, etapa):
    lista = []
    
    for indice in indices:
        #print("indice: " + str(indice['indice']))
        if(etapa == '7' or etapa == None):
            defeitos = DefeitoResultados2.objects.filter(indice=indice['indice'])
        elif(etapa != 7):
            defeitos = DefeitoResultados2.objects.filter(indice=indice['indice'], modo_defeito=etapa)
        for defeito in defeitos:
            #print(defeito)
            #########################################################################################################################
            ##Descrição do Local Defeito
            codigoLocalDefeito = defeito.cd_local_defeito.cd_local_defeito
            #print(codigoLocalDefeito)
            localDefeito = LocalDefeito.objects.filter(cd_local_defeito=codigoLocalDefeito).values('ds_local_defeito')
            descricaoLocalDefeito = localDefeito[0]['ds_local_defeito']
            #print(descricaoLocalDefeito)
            #########################################################################################################################
            ##Descrição do Tipo Defeito
            codigoDefeito = defeito.cd_defeito.cd_defeito
            #print(codigoDefeito)
            tipoDefeito = Defeito.objects.filter(cd_defeito=codigoDefeito).values('ds_defeito')
            descricaoTipoDefeito = tipoDefeito[0]['ds_defeito']
            #print(descricaoTipoDefeito)
            #########################################################################################################################
            ##Descrição Teste defeito
            codigoTeste = defeito.codigo
            #print(codigoTeste)
            teste = Testes.objects.filter(codigo=codigoTeste).values('descricao')
            descricaoTeste = teste[0]['descricao']
            #print(descricaoTeste)
            #########################################################################################################################
            ##Observação Defeito
            observacaoDefeito = defeito.sc_defeito
            #print(observacaoDefeito)
            #########################################################################################################################
            ##Etapa Defeito
            etapaDefeito = defeito.modo_defeito
            if(etapaDefeito == 0):
                descricaoEtapaDefeito = "Integração"
            elif(etapaDefeito == 1):
                descricaoEtapaDefeito = "Runin"
            elif(etapaDefeito == 2):
                descricaoEtapaDefeito = "Liberação"
            #print(descricaoEtapaDefeito)

            data = (indice['magnus'], indice['serie'], descricaoEtapaDefeito, descricaoTeste, descricaoLocalDefeito, descricaoTipoDefeito, observacaoDefeito)
            #print(data)
            lista.append(data)
    return lista

def GetDataHora(request):
    #Data enviada do formulario do front, na primeira vez sempre irá assumir data atual
    data_selecionada_inicio = request.GET.get('data_selecionada_inicio')
    
    if not data_selecionada_inicio:
        data_selecionada_inicio = datetime.now().strftime('%Y-%m-%d')  # Use the current date if no date is selected
        
    inicio_data_hora = datetime.strptime(data_selecionada_inicio, '%Y-%m-%d')
    #print(inicio_data_hora)
    
    data_selecionada_fim = request.GET.get('data_selecionada_fim')
    
    if not data_selecionada_fim:
        data_selecionada_fim = datetime.now().strftime('%Y-%m-%d')  # Use the current date if no date is selected
    
    fim_data_hora = datetime.strptime(data_selecionada_fim, '%Y-%m-%d')
    fim_data_hora = fim_data_hora.replace(hour=23, minute=59, second=59)
    #print(fim_data_hora)
    ##Retornos: 1° e 2° = data formatada para consulta no banco; 3° e 4°: Data formatada para enviar ao front
    return inicio_data_hora, fim_data_hora, data_selecionada_inicio, data_selecionada_fim

@login_required  # Aplica o decorator aqui
def defeitos(request):
        
    if request.method == "GET":
        
        etapa = request.GET.get('etapa')
        
        pesquisa = request.GET.get('searchCodigo')
        #print(pesquisa)
        
        #Chama função que retorna Data e Hora formatada para seus respectivos usos
        inicio_data_hora, fim_data_hora, data_selecionada_inicio, data_selecionada_fim = GetDataHora(request)
        
        #Se vier algo na Pesquisa (codigo)
        if(pesquisa != None and len(pesquisa) == 10):
            #Chama função que retorna os indices de maquinas entradas filtrado por data
            indices = retornaIndicesByCodigo(inicio_data_hora, fim_data_hora, pesquisa)
            
        else:
            #Chama função que retorna os indices de maquinas entradas filtrado por data
            indices = retornaIndicesByDate(inicio_data_hora, fim_data_hora)
        #print(indices)
        #Chama função que retorna lista dos defeitos formatados
        lista = GetDataDefeitos(indices, etapa)
        listaJson = json.dumps(lista)
        return render(request, 'defeitos.html', {'data': lista, 'datajson':listaJson, 'data_inicio':data_selecionada_inicio, 'data_fim':data_selecionada_fim, 'codigo': pesquisa, 'etapa': etapa})

    #Se o método da requisição for POST retorna excel
    if request.method == "POST":
        column_names = ['codigo', 'serie', 'etapa', 'teste', 'local_defeito', 'defeito', 'observacao']
        
        # Criar um DataFrame a partir da lista de dados
        df = pd.DataFrame(lista, columns=column_names)
        # Imprimir os nomes das colunas presentes no DataFrame
        print(df.columns)
        
        # Especificar o caminho do arquivo Excel de saída
        caminho_arquivo_excel = 'defeitos.xlsx'

        # Exportar os dados para o arquivo Excel
        df.to_excel(caminho_arquivo_excel, index=False)
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
            df.to_excel(tmp.name, index=False)
            tmp.seek(0)
            response = HttpResponse(tmp.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="defeitos.xlsx"'
            return response