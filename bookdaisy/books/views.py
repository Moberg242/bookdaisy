from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
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
    return render(req, 'home.html')

@login_required
def add_book(req):
    if req.method == 'POST':
        form = BookForm(req.POST, req.FILES)
        form.instance.user = req.user
        if form.is_valid():
          new_book = form.save(commit=False)
          # if new_book.image:
          #      new_book.image_data = form.cleaned_data['image'].file.read()
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
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def change_theme(req):
     profile = Profile.objects.get(user=req.user)
     if profile.darkTheme == True:
          profile.darkTheme = False
     else:
          profile.darkTheme = True
     profile.save()
     return redirect ('home')

class AddBook(LoginRequiredMixin, CreateView):
     model = Book
     fields = ['title', 'author', 'genre', 'rating', 'read', 'recommend', 'notes', 'image']

class UpdateBook(LoginRequiredMixin, UpdateView):
     model = Book
     fields = ['title', 'author', 'genre', 'rating', 'read', 'recommend', 'notes', 'image']
     success_url = '/library/title/'

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
          queryset = Book.objects.all().filter(Q(read=False)|Q(user=self.request.user))
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
