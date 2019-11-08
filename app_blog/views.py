from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, FormView
from .models import *
from .forms import PublicacaoForm, CommentForm
from django.http import HttpResponse

def inicio(request):
    pessoa = Pessoa.objects.get(usuario=request.user)
    seguidores = pessoa.seguidores.all()
    publicacoes = Publicacao.objects.filter(autor__in=seguidores).order_by('-id')[0:30]

    return render(request, 'app_blog/inicio.html', {'publicacoes': publicacoes})

def perfil(request, nome):
    try:
        pessoa = Pessoa.objects.get(usuario__username=nome)
        publicacoes = Publicacao.objects.filter(autor=pessoa).order_by('-id')[0:30]

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

class HomePageView(TemplateView):
    template_name = 'app_blog/home.html'


def pubs_detail(request, public_id):
    try:
        pub = Publicacao.objects.get(pk = public_id)
        comentarios = Comentario.objects.all()
        coments = comentarios.filter(publicacao=pub)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                print("val")
                form = form.save()
                form.refresh_from_db()
                form.publicacao = pub
                form.autor_comment = request.user
                form.save()
                return HttpResponseRedirect("/")
        else:
            form = CommentForm()

    except Publicacao.DoesNotExist:
        raise Http404('Publicação não encontrada')

    return render(request, 'app_blog/detalhe.html', {'pub':pub,'coments':coments,'form':form,})