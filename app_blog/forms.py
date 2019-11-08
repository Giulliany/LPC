from django import forms
from .models import *

class PublicacaoForm(forms.ModelForm):
    pub_text = forms.CharField(widget = forms.Textarea(attrs={'cols': 100, 'rows': 10}),required=True,max_length=200)

    class Meta:
        model = Publicacao
        fields = ('pub_text',)

class CommentForm(forms.ModelForm):
    coment = forms.CharField(widget=forms.Textarea,max_length=200)

    class Meta:
        model = Comentario
        fields = ('coment',)