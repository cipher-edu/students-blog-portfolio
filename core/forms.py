from django import forms
from .models import *


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'date': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control col-4'}),
            'category': forms.Select(attrs={'class':'form-control col-4'}),
            'title': forms.TextInput(attrs={'class':'form-control col-4'}),
            'content': forms.Textarea(attrs={'class':'form-control col-6'}),
            'image': forms.FileInput(attrs={'class': 'form-control col-4','enctype': 'multipart/form-data'}),
        }