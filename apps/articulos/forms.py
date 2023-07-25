from django import forms
from .models import Articulo

class ArticuloForms(forms.ModelForm):

    class Meta:
        model = Articulo
        fields = ['titulo','subtitulo','contenido','categoria','imagen']




   