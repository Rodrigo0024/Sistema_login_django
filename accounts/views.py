from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Bem-vindo, {user.username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, 'Você saiu da sua conta.')
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada com sucesso! Bem-vindo(a), {username}.')
            login(request, user)  # ← LOGA AUTOMATICAMENTE
            return redirect('dashboard')  # ← REDIRECIONA PARA DASHBOARD!
        else:
            # Se o formulário for inválido, mostra os erros
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = CustomUserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'accounts/dashboard.html')