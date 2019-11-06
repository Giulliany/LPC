from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import PublicacaoForm
from django.http import HttpResponse

def inicio(request):
    pessoa = Pessoa.objects.get(usuario=request.user)
    seguidores = pessoa.seguidores.all()
    publicacoes = Publicacao.objects.filter(autor__in=seguidores)

    return render(request, 'app_blog/inicio.html', {'publicacoes': publicacoes})

def perfil(request, nome):
    try:
        pessoa = Pessoa.objects.get(usuario__username=nome)
        publicacoes = Publicacao.objects.filter(autor=pessoa)
    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')

    return render(request, 'app_blog/perfil.html', {'publicacoes': publicacoes, 'pessoa': pessoa})
def comentario(request):
    return render(request, 'app_blog/comentario.html')
def DetalhePub(request, id_publicacao):
    try:
        pub = Publicacao.objects.get(pk=id_publicacao)
        comentario = Comentario.objects.filter(publicacao=pub)
    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')

    return render(request, 'app_blog/detalhe.html', {'pub': pub, 'comentario': comentario})

class PublicacaoView(FormView):
    template_name = 'app_blog/publicar.html'
    form_class = PublicacaoForm

    def form_valid(self, form):
        dados = form.clean()
        pessoa = Pessoa.objects.get(usuario=self.request.user)
        publicacao = Publicacao(texto=dados['texto'], autor=pessoa)
        publicacao.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('inicio')

def seguir(request, id_pessoa):
    try:
        pessoa = Pessoa.objects.get(usuario=request.user)
        seguir_pessoa = pessoa.objects.get(pk=id_pessoa)
        pessoa.seguidores.add(seguir_pessoa)

    except Exception as identifier:
        return HttpResponse('Objeto Não encontrado')

    return render(request, 'rede/sucesso_seguir.html', {'famosinho': cara_quero_seguir})

class HomePageView(TemplateView):
    template_name = 'app_blog/home.html'