from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

from main.models import Produto
from login.decorators import login_required  # Importa o decorator


@login_required  # Aplica o decorator aqui
def produto_list(request):
    
    if request.method == 'GET':
        controlseqprod = request.GET.get('controlseqprod')
        print (controlseqprod)
        ativo = request.GET.get('ativo')
        print(ativo)
        jiga = request.GET.get('jiga')
        print(jiga)
        ################################################################################################################################################
        ###DIFERENTES TIPOS DE RETORNO DE DADOS DA TABELA PRODUTO
        ###RETORNA SELECT COM TUDO
        if (controlseqprod == 'T' or controlseqprod == None) and (ativo == 'T' or ativo == None) and (jiga == 'T' or jiga == None):
            produtos = Produto.objects.all()
        ###RETORNA SELECT COM WHERE EM "controle_seq_prod = controlseqprod"
        elif (controlseqprod != 'T') and (ativo == 'T' or ativo == None) and (jiga == 'T' or jiga == None):
            produtos = Produto.objects.filter(controle_seq_prod__exact=controlseqprod)
        ###RETORNA SELECT COM WHERE EM "in_ativo = ativo"
        elif (ativo != 'T') and (controlseqprod == 'T' or controlseqprod == None) and (jiga == 'T' or jiga == None):
            produtos = Produto.objects.filter(in_ativo__exact=ativo)
        ###RETORNA SELECT COM WHERE EM "in_jiga = jiga"
        elif (jiga != 'T') and (controlseqprod == 'T' or controlseqprod == None) and (ativo == 'T' or ativo == None):
            produtos = Produto.objects.filter(in_jiga__exact=jiga)
        ###RETORNA SELECT COM WHERE EM "controle_seq_prod = controlseqprod and in_ativo = ativo"
        elif (controlseqprod != 'T') and (ativo != 'T') and (jiga == 'T' or jiga ==None):
            produtos = Produto.objects.filter(controle_seq_prod__exact=controlseqprod, in_ativo__exact=ativo)
        ###RETORNA SELECT COM WHERE EM "controle_seq_prod = controlseqprod and in_jiga = jiga"
        elif (controlseqprod != 'T') and (jiga != 'T') and (ativo == 'T' or ativo ==None):
            produtos = Produto.objects.filter(controle_seq_prod__exact=controlseqprod, in_jiga__exact=jiga)
        ###RETORNA SELECT COM WHERE EM "in_ativo = ativo and in_jiga = jiga"
        elif (ativo != 'T') and (jiga != 'T') and (controlseqprod == 'T' or controlseqprod ==None):
            produtos = Produto.objects.filter(in_ativo__exact=ativo, in_jiga__exact=jiga)
        ###RETORNA SELECT COM WHERE EM "controle_seq_prod = controlseqprod and in_ativo = ativo and in_jiga = jiga"
        elif controlseqprod != 'T' and ativo != 'T' and jiga != 'T':
            produtos = Produto.objects.filter(controle_seq_prod__exact=controlseqprod, in_ativo__exact=ativo, in_jiga__exact=jiga)

        #print(produtos)
        return render(request, 'produto.html', {'produtos':produtos, 'controleseqprod':controlseqprod, 'ativo':ativo, 'jiga':jiga})
    #Se efetuar uma pesquisa
    if request.method == 'POST':
        codigo = request.POST.get('search')
        print(codigo)
        produto = Produto.objects.filter(cd_produto__exact=codigo)
        return render(request, 'produto.html', {'produtos':produto})


def produto_insert(request):
    if request.method == 'GET':
        return render(request, 'produto_insert.html')
    
    ###INSERT DE PRODUTO
    if request.method == 'POST':
        ###PEGA OS DADOS PASSADO PELA REQUISIÇÃO(POST DA WEB)
        codigo = request.POST.get('codigo')
        print(codigo)
        descricao = request.POST.get('descricao')
        print(descricao)
        control_seq_prod = request.POST.get('contseqprod')
        print(control_seq_prod)
        ativo = request.POST.get('ativo')
        print(ativo)
        jiga = request.POST.get('jiga')
        print(jiga)
        ###SALVA OS VALORES NA VARIAVEL PRODUTO E SALVA O INSERT
        produto = Produto(cd_produto=codigo,ds_produto=descricao,controle_seq_prod=control_seq_prod,in_ativo=ativo,in_jiga=jiga,in_smp="N",exige_obs_teste='N',in_param_padrao='S',exige_com_jiga='S',exige_com_periferico='S')
        produto.save()
        
        return redirect()    
    

def produto_update(request, cd_produto):
    print(cd_produto)
    if request.method == 'GET':
        produto = Produto.objects.get(cd_produto__exact=cd_produto)
        print(produto.ds_produto)
        return render(request,'produto_update.html',{'produto':produto})
    elif request.method == 'POST':
        
        codigo = request.POST.get('codigo')
        print(codigo)
        descricao = request.POST.get('descricao')
        print(descricao)
        control_seq_prod = request.POST.get('contseqprod')
        print(control_seq_prod)
        ativo = request.POST.get('ativo')
        print(ativo)
        jiga = request.POST.get('jiga')
        print(jiga)
        ###SALVA OS VALORES NA VARIAVEL PRODUTO E SALVA O INSERT
        produto = Produto(cd_produto=codigo,ds_produto=descricao,controle_seq_prod=control_seq_prod,in_ativo=ativo,in_jiga=jiga,in_smp="N",exige_obs_teste='N',in_param_padrao='S',exige_com_jiga='S',exige_com_periferico='S')
        produto.save()
        
        return redirect()
    
    
def produto_delete(request, cd_produto):
    print(cd_produto)
    produto = Produto.objects.filter(cd_produto__exact=cd_produto)
    produto.delete()
    return redirect()

def redirect():
    return HttpResponseRedirect(reverse('produto'))