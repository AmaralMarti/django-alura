from django.shortcuts import render
from perfis.models import Perfil

def index(request):
    return render(request, 'index.html')

def exibir(request, perfil_id):

    try:
    	perfil = Perfil.objects.get(id=perfil_id)
    	return render(request, 'perfil.html', {'perfil': perfil})
    except Exception, e:
    	return render(request, 'perfilinvalido.html', {'perfil_id': perfil_id})