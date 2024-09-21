from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from colorfield.widgets import ColorWidget
from django.forms.utils import ErrorList
from django.forms import ModelChoiceField
from .models import Book

# class ColorInput(forms.widgets.Input):
#     input_type = 'color'

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','genre','read', 'read', 'recommend', 'notes', 'image']



class ShelfForm(ModelForm):
    class Meta:
        model = Book
        fields = ['color', 'text_color']
        widgets = {
            'color':ColorWidget,
        }
