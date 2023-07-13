from django import forms
from AppChat.models import Mensaje

class CommentForm(forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ('autorMensaje', 'texto')