from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from pyexpat import model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Book
from .forms import BookForm

# Create your views here.
def home(req):
    return render(req, 'home.html')

def index(req):
     return render(req, 'books/index.html', {'sorted':'title'})

def add_book(req):
    if req.method == 'POST':
        form = BookForm(req.POST, req.FILES)
        if form.is_valid():
            new_book = form.save(commit=False)
            # if new_book.image:
            #      new_book.image_data = form.cleaned_data['image'].file.read()
            new_book.save()
            return redirect('home')
    else:
            form = BookForm()
    return render(req, 'books/book_form.html', {'form':form})

class UpdateBook(UpdateView):
     model = Book
     fields = '__all__'
     success_url = '/library/'

class DeleteBook(DeleteView):
     model = Book
     success_url = '/library/'

class Index(ListView):
    model = Book
    template_name = 'books/index.html'

class SearchTitle(ListView):
     model = Book
     template_name = 'books/search.html'
     
     def get_queryset(self):
          query = self.request.GET.get('q')
          queryset = Book.objects.all().filter(title__icontains=query)
          return queryset

class BookDetails(DetailView):
     model = Book
     template_name = 'books/details.html'
