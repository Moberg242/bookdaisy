from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.contrib.auth.forms import UserChangeForm
from django.forms import ModelForm
from django import forms
from colorfield.widgets import ColorWidget
from django.forms.utils import ErrorList
from django.forms import ModelChoiceField
from django.contrib.auth.models import User
from .models import Book, Profile

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','genre','read', 'read', 'recommend', 'notes', 'color', 'text_color', 'image']
        widgets = {
            'color':ColorWidget,
            'text_color':ColorWidget
        }

class ShelfForm(ModelForm):
    class Meta:
        model = Book
        fields = ['color', 'text_color']
        widgets = {
            'color':ColorWidget,
            'text_color':ColorWidget
        }

class ShelfColor(ModelForm):
    class Meta:
        model = Profile
        fields = ['color']
        widgets = {
            'color':ColorWidget,
        }

class ProfileForm(ModelForm):
    email = forms.EmailField(label='email', widget=forms.TextInput())
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['username'].initial = user.username
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name
            self.fields['email'].initial = user.email