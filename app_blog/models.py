from django.db import models
from django.contrib.auth.models import User


class Pessoa(models.Model):
    usuario = models.ForeignKey(User, verbose_name='Autor', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=60, blank=True, null=True)
    seguidores = models.ManyToManyField("Pessoa", verbose_name='Seguidores', blank=True, null=True)

    def __str__(self):
        return self.usuario.username


class Publicacao(models.Model):
    texto = models.TextField(verbose_name='Texto', max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Pessoa, verbose_name='Autor', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.texto


class Comentario(models.Model):
    texto = models.TextField(verbose_name='Texto', max_length=200)
    data = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(Pessoa, related_name='autor', on_delete=models.DO_NOTHING)
    publicacao = models.ForeignKey(Publicacao, related_name='publicacao', on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.texto


