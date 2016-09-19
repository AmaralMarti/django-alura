from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):

    perfil = Perfil()

    if perfil_id == '1':
    	perfil = Perfil('Henrique', 'henrique@henrique.com.br', '12345678', 'empresa')  
    	return render(request, 'perfil.html', {'perfil': perfil})
    else:
    	return render(request, 'perfilinvalido.html', {'perfil_id': perfil_id})