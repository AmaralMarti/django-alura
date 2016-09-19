from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html', {'perfis': Perfil.objects.all()})

def exibir(request, perfil_id):
    
    try:
    	perfil = Perfil.objects.get(id=perfil_id)    	
    except Exception:
    	perfil = None

    return render(request, 'perfil.html', {'perfil': perfil, 'perfil_id': perfil_id})	