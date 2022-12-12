from django import forms
from .models import Project

class CreateNewProject(forms.Form):
    title = forms.CharField(label="Titulo del projecto",max_length=200)
    description = forms.CharField(label="Descripcion del projecto", widget=forms.Textarea)
    foto = forms.ImageField()
    tag = forms.CharField(max_length=100)
    url_git = forms.URLField()

    # class Meta:
    #     model = Project
    #     widgets = {
    #         'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe el titulo'}),
    #         'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Escribe la descripcion'}),
    #         'foto': forms.TextInput(attrs={'class':'form-control'}),
    #         'tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escribe las tags'}),
    #         'url_git': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Intriduce una direccion URL'}),

    #     }
