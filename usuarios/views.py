from django.shortcuts import render, redirect
from django.views.generic.base import View
from usuarios.forms import RegistrarUsuarioForm
from django.contrib.auth.models import User
from perfis.models import Perfil


class RegistrarUsuarioView(View):

	template_name = 'registrar.html'
	def get(self, request):
		return render(request, self.template_name)

	def post(self, request):
		form = RegistrarUsuarioForm(request.POST)
		if form.is_valid():
			dados = form.data

			usuario = User.objects.create_user(dados['nome'], dados['email'], dados['senha'])
			perfil = Perfil(nome=dados['nome'], telefone=dados['telefone'], nome_empresa=dados['nome_empresa'], usuario=usuario)
			perfil.save()

			return redirect('index')


		return render(request, self.template_name, {'form': form})
		
