from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
#.models = arquivo onde estão as tabelas do bando - Usuarios = nome da tabela do banco
from main.models import Usuarios, Acesso

#Pagina Inicial do sistema
def home(request):
    return render(request,'home.html')
    
def usuarios_list(request):
    if request.method == 'GET':
        '''usuarios=Usuarios.objects.all()
        acessos=Acesso.objects.all()
        
        #print(usuarios[0].nome)
        #Retornar os dados para a pagina - Envia a variavel "usuario para a pagina especificada"
        return render(request,'usuarios.html',{'usuarios': usuarios, 'acessos': acessos})'''
        #Pega status enviado pelo front
        status = request.GET.get('status')
        acesso = request.GET.get('acesso')
        #Decide o que vai enviar a partir do select de in_ativo
        if status == 'T' and acesso == '1' or acesso == None or status == None and acesso == '1':
            usuarios=Usuarios.objects.all()
        elif status != 'T' and acesso == '1':
            usuarios=Usuarios.objects.filter(in_ativo=status)
        elif status != 'T' and acesso != '1':
            usuarios=Usuarios.objects.filter(in_ativo=status, cd_acesso=acesso)
        elif status == 'T' and acesso != '1':
            usuarios=Usuarios.objects.filter(cd_acesso=acesso)    
        
        #Instancia classe Acesso
        cd_acesso = Acesso.objects.all()
            
        # Lista de tuplas (matricula, nome, senha, cd_acesso, in_ativo, ds_acesso)
        usuarios_com_acesso = [(usuario.matricula, usuario.nome, usuario.senha, usuario.cd_acesso.ds_acesso, usuario.in_ativo) for usuario in usuarios]
        return render(request, 'usuarios.html', {'usuarios': usuarios_com_acesso, 'status':status, 'cd_acessos':cd_acesso, 'acesso':acesso}) #usuario = toda lista de usuarios; status=retorno do html de qual status fazer a requisição; cd_acesso=lista de acessos; acesso=qual acesso vai pesquisar

    elif request.method == 'POST':

        search = request.POST.get('search')
        usuarios=Usuarios.objects.filter(matricula__exact=search)
        status = 'S'
        # Lista de tuplas (matricula, nome, senha, cd_acesso, in_ativo, ds_acesso)
        usuarios_com_acesso = [(usuario.matricula, usuario.nome, usuario.senha, usuario.cd_acesso.ds_acesso, usuario.in_ativo) for usuario in usuarios]
        return render(request, 'usuarios.html', {'usuarios': usuarios_com_acesso, 'status':status})
    
def usuarios_insert(request):
    if request.method == 'GET':
        acesso = Acesso.objects.all()
        print(acesso)
        return render(request,'usuarios_insert.html',{'acesso':acesso})
    
    elif request.method == 'POST':
        #Pega os dados enviados pelo formulario e salva nas variaveis
        matricula = request.POST.get('matricula')
        nome = request.POST.get('nome')
        senha = request.POST.get('password')
        acesso = request.POST.get('acesso')
        cd_acesso = Acesso.objects.get(cd_acesso=acesso)
        ativo = request.POST.get('ativo')
        #cria a variavel usuario para receber os dados
        usuario = Usuarios(nome=nome, matricula=matricula, senha=senha, cd_acesso=cd_acesso, in_ativo=ativo)
        #salva a variavel usuario
        usuario.save()
        
        return redirect()   
        #return render(request,'usuarios.html',{'usuarios': usuarios})

def usuarios_update(request, matricula):
    if request.method == 'POST':
        #Pega os dados enviados pelo formulario e salva nas variaveis
        nome = request.POST.get('nome')
        cd_matricula = request.POST.get('matricula')
        senha = request.POST.get('password')
        acesso = request.POST.get('acesso')
        cd_acesso = Acesso.objects.get(cd_acesso=acesso)
        ativo = request.POST.get('ativo')
        
        print(cd_acesso)
        #cria a variavel usuario para receber os dados
        usuario = Usuarios(nome=nome, matricula=cd_matricula, senha=senha, cd_acesso=cd_acesso, in_ativo=ativo)
        #salva a variavel usuario
        usuario.save()
        
        return redirect()
    
    elif request.method == 'GET':
        usuario = Usuarios.objects.get(matricula__exact=matricula)
        acessos=Acesso.objects.all()
        print(usuario.matricula)
        return render(request,'usuarios_update.html',{'usuario': usuario, 'acessos': acessos})
      
def usuarios_delete(request, matricula):
    usuario = Usuarios.objects.filter(matricula__exact=matricula)
    usuario.delete()

    return redirect()

def redirect():
    return HttpResponseRedirect(reverse('usuarios'))