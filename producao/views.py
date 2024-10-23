from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.models import Producao, Resultados, Usuarios, Testes, Medidas

from django.db.models import F, Window
from django.db.models.functions import RowNumber

from datetime import datetime
import pandas as pd
import tempfile
import pytz
from django.http import JsonResponse

def sdp(inicio_data_hora, fim_data_hora):

    # Lista de valores de NRO_SERIE a serem excluídos
    nro_serie_excluidos = list(range(11))

    # Execute a consulta usando o ORM do Django
    queryset = Producao.objects.filter(
        dt_fim_prod__range=(inicio_data_hora, fim_data_hora)
    ).exclude(
        nro_serie__in=nro_serie_excluidos
    ).values(
        'cd_produto', 'nro_serie'
    ).distinct()
    
    return queryset

def detalha_sdp(codigo, ns):
    # Subconsulta para adicionar a coluna RowNum
    resultados_com_rownumber = Resultados.objects.filter(
        magnus=codigo,
        serie=ns
    ).annotate(
        rownum=Window(
            expression=RowNumber(),
            partition_by=[F('magnus'), F('serie')],
            order_by=F('indice').desc()
        )
    )
    
    # Filtrar para obter apenas os registros com RowNum = 1
    resultados_filtrados = resultados_com_rownumber.filter(rownum=1).order_by('magnus')
    
    return resultados_filtrados

def search_atm(ns):
    # Lista de valores de NRO_SERIE a serem excluídos
    nro_serie_excluidos = list(range(11))

    # Execute a consulta usando o ORM do Django
    queryset = Producao.objects.filter(
        nro_serie=ns
    ).exclude(
        nro_serie__in=nro_serie_excluidos
    ).values(
        'cd_produto', 'nro_serie'
    ).distinct()
    
    #print(queryset)
    maquina = queryset[0]
    codigo = maquina['cd_produto']
    
    #Chama função que traz os detalhes da producao para cada numero de serie
    producao_detalhada = detalha_sdp(codigo, ns)
    print(producao_detalhada)
    
    for producao in producao_detalhada:

                    
        ##############################################PRODUTO##################################################
        #Salva objeto "Modelo" que esta vindo do Select da tabela Resultados na variavel produto
        produto = producao.magnus
        #print(produto)
        #Pega o magnus do Objeto Modelo (que seria o código do atm)
        magnus_produto = produto.magnus
        #print(magnus_produto)
        ########################################################################################################
        
        ############################################USUARIO-INTEGRAÇÃO##########################################
        usuario = producao.matricula
        #print(usuario)
        nome_usuario = usuario.nome
        #print("Usuario Integração: " + nome_usuario)
        ########################################################################################################

        ############################################USUARIO-RUNIN##############################################
        if producao.matricula_runin != None:
            usuario_runin = Usuarios.objects.get(matricula=producao.matricula_runin)
            nome_usuario_runin = usuario_runin.nome
            #print("Usuario Runin: " + nome_usuario_runin)
        elif producao.matricula_runin == None:
            nome_usuario_runin = None
        ########################################################################################################
        
        ############################################USUARIO-LIBERAÇÃO##############################################
        if producao.matricula_liberacao != None:
            usuario_liberacao = Usuarios.objects.get(matricula=producao.matricula_liberacao)
            nome_usuario_liberacao = usuario_liberacao.nome
            #print("Usuario Runin: " + nome_usuario_runin)
        elif producao.matricula_liberacao == None:
            nome_usuario_liberacao = None
        ########################################################################################################
        
        resultado = (producao.indice, magnus_produto, producao.serie, producao.dataini, producao.datafim, producao.modos, nome_usuario, nome_usuario_runin, nome_usuario_liberacao)

        
        #print(resultado)
    
    return resultado

# Create your views here.
def producao_list(request):
    
    #Data enviada do formulario do front, na primeira vez sempre irá assumir data atual
    data_selecionada_inicio = request.GET.get('data_selecionada_inicio')
    
    if not data_selecionada_inicio:
        data_selecionada_inicio = datetime.now().strftime('%Y-%m-%d')  # Use the current date if no date is selected
        
    inicio_data_hora = datetime.strptime(data_selecionada_inicio, '%Y-%m-%d')
    print(inicio_data_hora)
    
    data_selecionada_fim = request.GET.get('data_selecionada_fim')
    
    if not data_selecionada_fim:
        data_selecionada_fim = datetime.now().strftime('%Y-%m-%d')  # Use the current date if no date is selected
    
    fim_data_hora = datetime.strptime(data_selecionada_fim, '%Y-%m-%d')
    fim_data_hora = fim_data_hora.replace(hour=23, minute=59, second=59)
    print(fim_data_hora)
    
    #Lista zerada para enviar ao front
    lista_resultados = []
    
    liberadas = 0
    
    queryset = sdp(inicio_data_hora, fim_data_hora)    #Chama função que retorna dados SDP
    #print(queryset)
    for qs in queryset:
        codigo = qs['cd_produto']
        ns = qs['nro_serie']

        #Chama função que traz os detalhes da producao para cada numero de serie
        producao_detalhada = detalha_sdp(codigo, ns)
        
        # Executar a consulta e obter os resultados
        for producao in producao_detalhada:
            #Variaveis para conversões de data
            datafimsalvo = None
            datafimwhere = None
                        
            ##############################################PRODUTO##################################################
            #Salva objeto "Modelo" que esta vindo do Select da tabela Resultados na variavel produto
            produto = producao.magnus
            #print(produto)
            #Pega o magnus do Objeto Modelo (que seria o código do atm)
            magnus_produto = produto.magnus
            #print(magnus_produto)
            ########################################################################################################
            
            ############################################USUARIO-INTEGRAÇÃO##########################################
            usuario = producao.matricula
            #print(usuario)
            nome_usuario = usuario.nome
            #print("Usuario Integração: " + nome_usuario)
            ########################################################################################################

            ############################################USUARIO-RUNIN##############################################
            if producao.matricula_runin != None:
                usuario_runin = Usuarios.objects.get(matricula=producao.matricula_runin)
                nome_usuario_runin = usuario_runin.nome
                #print("Usuario Runin: " + nome_usuario_runin)
            elif producao.matricula_runin == None:
                nome_usuario_runin = None
            ########################################################################################################
            
            ############################################USUARIO-LIBERAÇÃO##############################################
            if producao.matricula_liberacao != None:
                usuario_liberacao = Usuarios.objects.get(matricula=producao.matricula_liberacao)
                nome_usuario_liberacao = usuario_liberacao.nome
                #print("Usuario Runin: " + nome_usuario_runin)
            elif producao.matricula_liberacao == None:
                nome_usuario_liberacao = None
            ########################################################################################################
            
            resultado = (producao.indice, magnus_produto, producao.serie, producao.dataini, producao.datafim, producao.modos, nome_usuario, nome_usuario_runin, nome_usuario_liberacao)
            if producao.modos == 7:
                liberadas += 1
            
            #print(resultado)
            ################################################################################################################################
            #Condição para incluir na lista apenas atms com datafim até a data selecionada e atms que não tiverem datafim - Seguindo o padrão do SDP
            datafimwhere = fim_data_hora.date()
            if producao.datafim != None:
                datafimsalvo = producao.datafim.date() 
            

            #print(datafimsalvo)
            #print(datafimwhere)
            if datafimsalvo == None:
                lista_resultados.append(resultado)
            elif datafimsalvo <= datafimwhere:
                lista_resultados.append(resultado)
            ################################################################################################################################
            
    if request.method == 'GET':
        #return HttpResponse("Producao")
        print(liberadas)
        return render(request, 'producao.html',{'producao':lista_resultados, 'data_inicio':data_selecionada_inicio, 'data_fim':data_selecionada_fim, 'liberadas':liberadas})
    
    if request.method == 'POST':
        #Tentativa de exportar a lista para excel
        pesquisa = request.POST.get('search')
        print(pesquisa)
        
        
        if pesquisa != None:
            atm = search_atm(pesquisa)
            print(atm)
            return render(request, 'producao_search.html',{'producao':atm, 'data_inicio':data_selecionada_inicio, 'data_fim':data_selecionada_fim, 'liberadas':liberadas})
        else:
        
            column_names = ['indice', 'codigo', 'serie', 'data_inicio', 'data_fim', 'etapa', 'integracao', 'runin', 'liberacao']
            
            # Criar um DataFrame a partir da lista de dados
            df = pd.DataFrame(lista_resultados, columns=column_names)
            # Imprimir os nomes das colunas presentes no DataFrame
            print(df.columns)

            # Antes de exportar, remova as informações de fuso horário dos datetimes
            df['data_inicio'] = df['data_inicio'].dt.tz_localize(None)
            df['data_fim'] = df['data_fim'].dt.tz_localize(None)
            
            # Especificar o caminho do arquivo Excel de saída
            caminho_arquivo_excel = 'dados.xlsx'

            # Exportar os dados para o arquivo Excel
            df.to_excel(caminho_arquivo_excel, index=False)
            
            with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
                df.to_excel(tmp.name, index=False)
                tmp.seek(0)
                response = HttpResponse(tmp.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
                response['Content-Disposition'] = 'attachment; filename="producao.xlsx"'
                return response


            
            #return redirect()    


def producao_detalha(request, codigo, nserie):
    
    operador = None
    desc_teste = None
    detalhes = None
    lista_detalhes = []

    producoes = Producao.objects.filter(cd_produto=codigo, nro_serie=nserie).order_by('dt_ini_prod')
    
    usuarios = Usuarios.objects.all()
    
    testes = Testes.objects.all()
    
    for produto in producoes:
        for usuario in usuarios:
            if usuario.matricula == produto.matricula:
                operador = usuario.nome
        
        for teste in testes:
            if teste.codigo == produto.codigo:
                desc_teste = teste.descricao
        
        detalhes = (codigo, nserie, operador, produto.dt_ini_prod, produto.dt_fim_prod, produto.modos, produto.estado, desc_teste)
        
        lista_detalhes.append(detalhes)
    
    if request.method == 'GET':
        #print(lista_detalhes)
        return render(request, 'producao_detalhe.html',{'producoes':lista_detalhes, 'codigo':codigo, 'nserie':nserie})
    
    if request.method == 'POST':
        #Tentativa de exportar a lista para excel
               
        column_names = ['codigoProduto', 'serie', 'operador', 'data_inicio', 'data_fim', 'etapa', 'estado', 'teste']
        
        # Criar um DataFrame a partir da lista de dados
        df = pd.DataFrame(lista_detalhes, columns=column_names)
        # Imprimir os nomes das colunas presentes no DataFrame
        print(df.columns)

        # Antes de exportar, remova as informações de fuso horário dos datetimes
        df['data_inicio'] = df['data_inicio'].dt.tz_localize(None)
        df['data_fim'] = df['data_fim'].dt.tz_localize(None)
        
        # Especificar o caminho do arquivo Excel de saída
        caminho_arquivo_excel = 'dados_'+codigo+'_'+nserie+'.xlsx'

        # Exportar os dados para o arquivo Excel
        df.to_excel(caminho_arquivo_excel, index=False)
        
        with tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx') as tmp:
            df.to_excel(tmp.name, index=False)
            tmp.seek(0)
            response = HttpResponse(tmp.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename="producao.xlsx"'
            return response

def producao_medidas(request, codigo, nserie):

    lista_medidas = []
    medidas = Medidas.objects.filter(cd_produto=codigo, nro_serie=nserie)
    for m in medidas:
        ###################################TIPO MEDIDA###################################
        if m.id_tp_medida == 112:
            tipo_medida = "Resistência (Ohms)"
        elif m.id_tp_medida == 483:
            tipo_medida = "Conversor Analógico Digital"
        #################################################################################
        ###################################TIPO MEDIDA###################################
        if m.id_tp_local == 468:
            tipo_local = "Malha Elétrica 1"
        elif m.id_tp_local == 469:
            tipo_local = "Malha Elétrica 2"
        elif m.id_tp_local == 470:
            tipo_local = "Malha Elétrica 3"
        elif m.id_tp_local == 471:
            tipo_local = "Malha Elétrica 4"
        elif m.id_tp_local == 472:
            tipo_local = "Malha Elétrica 5"
        elif m.id_tp_local == 484:
            tipo_local = "Zona 1"
        #################################################################################
        ###################################RESULTADO###################################
        if m.resultado == "A":
            result = "Aprovado"
        elif m.resultado == "R":
            result = "Reprovado"
        #################################################################################
        
        medida = (tipo_medida, tipo_local, m.medida, m.max, m.min, m.dt_medida, result)
        lista_medidas.append(medida)
    #medidas_list = list(medidas.values('id_tp_medida', 'id_tp_local', 'medida', 'max', 'min', 'dt_medida', 'resultado'))
    return JsonResponse(lista_medidas, safe=False)
    


def redirect():
    return HttpResponseRedirect(reverse('producao'))