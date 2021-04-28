from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if not nome.strip():
            print('O campo nome não pode ficar em branco')
        if not email.strip():
            print('O campo email não pode ficar em branco')
            return render(request, 'usuarios/cadastro.html')
        if password != password2:
            print('As passwords não são iguais')
            return render(request, 'usuarios/cadastro.html')
        if User.objects.filter(email=email).exists():
            print('Usiário já cadastrado')
            return render(request, 'usuarios/cadastro.html')
        user = User.objects.create_user(username=nome, email=email, password=password)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        if email == "" or senha == "":
            print("Os campos não podem ficar embranco")
            return render(request, 'usuarios/login.html')
        print(email, senha)
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            user = auth.authenticate(request, username=nome, password=senha)
            if user is not None:
                auth.login(request, user)
                print('login realizado com sucesso')
                return redirect('dashboard')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    else:
        return redirect('index')

def logout(request):
    auth.logout(request)
    return redirect('index')

def cria_receita(request):
    if request.method == 'POST':
        nome_receita = request.POST['nome_receita']
        ingredientes = request.POST['ingredientes']
        modo_preparo = request.POST['modo_preparo']
        tempo_preparo = request.POST['tempo_preparo']
        rendimento = request.POST['rendimento']
        categoria = request.POST['categoria']
        foto_receita = request.FILES['foto_receita']
        rendimento = request.POST['rendimento']

        print(nome_receita, ingredientes, modo_preparo, tempo_preparo, 
        rendimento, categoria, foto_receita)

        return redirect('dashboard')
    else:
        return render(request, 'usuarios/cria_receita.html')