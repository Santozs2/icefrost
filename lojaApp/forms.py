from django import forms 
from .models import sorvete, comentario

class SorveteForm(forms.ModelForm):
    class Meta:
        model = sorvete 
        fields = '__all__'

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = comentario
        fields = '__all__'