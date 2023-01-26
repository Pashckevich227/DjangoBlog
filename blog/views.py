from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView,)
from .models import Post
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'blog.add_post'
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
    success_url = reverse_lazy('home')


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'blog.change_post'
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class BlogDeleteView(DeleteView):
    permission_required = 'blog.delete_post'
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class LoginView(ListView):
    model = Post
    template_name = 'login.html'

