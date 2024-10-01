from typing import Any
# from django.db.models.query import QuerySet
from django.db.models import Q
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat import model
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django import template
from .models import Book, Profile
from .forms import BookForm, ShelfForm, ShelfColor

register = template.Library()

# Create your views here.
def about(req):
     return render(req, 'about.html')

def explore(req):
    profiles = Profile.objects.all()
    return render(req, 'explore.html', {'profiles':profiles})

@login_required
def edit_profile(req):
    pass
    # user = User.objects.get(id=req.user.id)
    # if req.method == 'POST':
    #     form = ProfileForm(req.POST, instance=user)
    #     if form.is_valid():
    #         form.save()
    #         login(req, user)
    #         return redirect('profile')
    # form = ProfileForm(instance=req.user)
    # return render(req, 'users/edit_profile.html', {'form':form})
            

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('explore')
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

class AddBook(LoginRequiredMixin, CreateView):
     model = Book
     fields = ['title', 'author', 'genre', 'read', 'image']

     def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)

class UpdateBook(LoginRequiredMixin, UpdateView):
     model = Book
     fields = ['title', 'author', 'genre', 'rating', 'read', 'recommend', 'notes','color', 'text_color', 'image']

class DeleteBook(LoginRequiredMixin, DeleteView):
     model = Book
     success_url = '/library/title/'

class Index(LoginRequiredMixin, ListView):
    model = Book
    template_name = 'books/index.html'

    def get_queryset(self):
        page_range = self.kwargs['page'] * 10
        start = page_range - 10
        queryset = Book.objects.all().filter(user=self.request.user).order_by(self.kwargs['sorted'])
        return queryset[start:page_range]

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


'''bookshelf views'''
@login_required
def home(req, pk):
    books = Book.objects.all().filter(Q(bookshelf=True) & Q(user=pk))
    profile = User.objects.get(id=pk)

    if req.method == 'POST':
        user = req.user.profile
        user2 = profile.profile
        print(user)
        print(profile.profile)
        action = req.POST['follow']
        if action == 'unfollow':
            user.follows.remove(user2)
        elif action == 'follow':
            user.follows.add(user2)
        user.save()

    return render(req, 'books/bookshelf/home.html', {'books':books, 'pk':pk, 'profile':profile})

@login_required
def add(req, **pk):
    if req.method == 'POST':
        data = req.POST
        book = Book.objects.all().get(Q(user=req.user) & Q(title=data['title']))
        book.bookshelf = True
        book.position = data['position']
        book.color = data['color']
        book.text_color = data['text_color']
        book.save()
        return redirect('edit_bookshelf')
    else:
         form = ShelfForm(initial={'bookshelf':True})
         color_form = ShelfColor(initial={'color':req.user.profile.color})
         books = Book.objects.all().filter(user=req.user)
         avail_books = Book.objects.all().filter(Q(user=req.user) & Q(bookshelf=False))
         positions = [1, 2, 3, 4]
         context = {'form':form, 'color_form':color_form, 'books':books, 'positions':positions, 'avail_books':avail_books}
    return render(req, 'books/bookshelf/edit_bookshelf.html', context)

@login_required
def remove(req, book_id):
    url = req.META.get('HTTP_REFERER')
    book = Book.objects.all().get(id=book_id)
    book.bookshelf = False
    book.position = None
    book.save()
    return redirect(url)

@login_required
def shelf_color(req):
     profile = Profile.objects.get(user=req.user)
     if req.method == 'POST':
         color = req.POST['color']
         profile.color = color
         profile.save()
     url = req.META.get('HTTP_REFERER')
     return redirect (url)

