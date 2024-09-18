from typing import Any, Mapping
from django.core.files.base import File
from django.db.models.base import Model
from django.forms import ModelForm
# from django import forms
# from django.forms.widgets import TextInput
from colorfield.widgets import ColorWidget
from django.forms.utils import ErrorList
from .models import Book

# class ColorInput(forms.widgets.Input):
#     input_type = 'color'

class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','genre','read', 'read', 'recommend', 'notes', 'color', 'text_color', 'image']
        widgets = {
            'color': ColorWidget,
        }

