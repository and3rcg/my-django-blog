from django.forms import ModelForm
from .models import Comentario

class FormComentario(ModelForm):
    def clean(self):
        data = self.cleaned_data
        nome = data.get('nome_comentario')
        email = data.get('email_comentario')
        comentario = data.get('comentario')

        if len(comentario) < 3:
            self.add_error('comentario', 'O comentário precisa possuir pelo menos 3 caracteres.')

    class Meta:
        model = Comentario
        fields = ('nome_comentario','email_comentario','comentario')