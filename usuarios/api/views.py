from django.shortcuts import render, redirect
from django.contrib.auth.models import User

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
        return render(request, 'usuarios/dashboard.html')
    return render(request, 'usuarios/login.html')

def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

def logout(request):
    pass
