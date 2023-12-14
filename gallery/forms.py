from django import forms
from .models import Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = ('__all__')
