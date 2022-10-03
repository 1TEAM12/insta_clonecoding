from django.shortcuts import render
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView)
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from user.models import User
from .forms import PostForm,ProfileForm

# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = "posts"
    ordering = ["-created_at"]

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/post_detail.html"
    pk_url_kwarg = "post_id"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post/new_post.html"
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("post-detail", kwargs={"post_id": self.object.id})

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin , UpdateView):
    model = Post
    form_class = PostForm
    template_name = "post/new_post.html"
    pk_url_kwarg = "post_id"
    
    raise_exception = True
    
    def get_success_url(self):
        return reverse("post-detail", kwargs={"post_id": self.object.id})
    
    def test_func(self, user):
        post = self.get_object()
        return post.author == user

    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "post/post_confirm_delete.html"
    pk_url_kwarg = "post_id"
    
    raise_exception = True

    def get_success_url(self):
        return reverse("index")
    
    def test_func(self, user):
        post = self.get_object()
        return post.author == user


class ProfileView(DetailView):
    model = User
    template_name = "post/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_id = self.kwargs.get("user_id")
        context["user_post"] = Post.objects.filter(author__id=user_id).order_by("-created_at")
        return context

class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "post/profile_set_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("index")

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "post/profile_update_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("profile", kwargs=({"user_id": self.request.user.id}))