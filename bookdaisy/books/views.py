from typing import Any
# from django.db.models.query import QuerySet
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from pyexpat import model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import template
from .models import Book, Profile
from .forms import BookForm

register = template.Library()

# Create your views here.
def about(req):
     return render(req, 'about.html')

@login_required
def home(req):
    books = Book.objects.all().filter(Q(bookshelf=True) & Q(user=req.user))
    return render(req, 'books/home.html', {'books':books})

@login_required
def add_book(req):
    if req.method == 'POST':
        form = BookForm(req.POST, req.FILES)
        if form.is_valid():
          new_book = form.save(commit=False)
          new_book.save()
          return redirect('home')
    else:
          form = BookForm()
    return render(req, 'books/book_form.html', {'form':form})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def change_theme(req):
     profile = Profile.objects.get(user=req.user)
     url = req.META.get('HTTP_REFERER')
     if profile.darkTheme == True:
          profile.darkTheme = False
     else:
          profile.darkTheme = True
     profile.save()
     return redirect (url)

class EditShelf(LoginRequiredMixin, ListView):
    model = Book
    fields = ['bookshelf', 'position', 'color', 'text_color']
    template_name = 'books/edit_bookshelf.html'

    def get_queryset(self):
        queryset = Book.objects.all().filter(user=self.request.user)
        return queryset

class AddBook(LoginRequiredMixin, CreateView):
     model = Book
     fields = ['title', 'author', 'genre', 'read', 'image']

     def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)

class UpdateBook(LoginRequiredMixin, UpdateView):
     model = Book
     fields = ['title', 'author', 'genre', 'rating', 'read', 'recommend', 'notes', 'color', 'text_color', 'image']

class DeleteBook(LoginRequiredMixin, DeleteView):
     model = Book
     success_url = '/library/title/'

class Index(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/index.html'

    def get_queryset(self):
        queryset = Book.objects.all().filter(user=self.request.user)
        return queryset.order_by(self.kwargs['sorted'])
#     help from django docs

class Tbr(LoginRequiredMixin, ListView):
     model = Book
     template_name = 'books/tbr.html'

     def get_queryset(self):
          queryset = Book.objects.all().filter(Q(read=False) & Q(user=self.request.user))
          return queryset.order_by(self.kwargs['sorted'])

class SearchTitle(LoginRequiredMixin, ListView):
     model = Book
     template_name = 'books/search.html'
     
     def get_queryset(self):
          query = self.request.GET.get('q')
          queryset = Book.objects.all().filter(user=self.request.user)
          queryset = queryset.filter(Q(title__icontains=query)|Q(author__icontains=query))
          return queryset

class BookDetails(LoginRequiredMixin, DetailView):
     model = Book
     template_name = 'books/details.html'
