from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    View,
    ListView, 
    DetailView, 
    CreateView, 
    UpdateView,
    DeleteView,
)
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q 
from braces.views import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Comment, Like
from user.models import User
from .forms import PostForm, ProfileForm, CommentForm
# Create your views here.

#post 팔로우한 사람만 나오는 페이지
class IndexView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/index.html"
    context_object_name = "posts"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['users'] = User.objects.all()
        context['comment_ctype_id'] = ContentType.objects.get(model='comment').id
        
        user = self.request.user
        if user.is_authenticated:
            context['likes_post'] = Like.objects.filter(user=user).exists()            
        return context 
    
#Post 모든 페이지    
class AllPostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "post/all_post.html"
    context_object_name = "posts"

#검색기능
class SearchView(ListView):
    model = Post
    context_object_name = 'search_results'
    template_name = 'post/search_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('query','')
        return Post.objects.filter(
            Q(content__icontains=query)
        )
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET.get('query','') 
        return context
    
    
#post상세페이지
class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post/post_detail.html"
    pk_url_kwarg = "post_id"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['post_ctype_id'] = ContentType.objects.get(model='post').id
        context['comment_ctype_id'] = ContentType.objects.get(model='comment').id
        
        user = self.request.user
        if user.is_authenticated:
            context['likes_post'] = Like.objects.filter(user=user).exists()
        return context

#post생성
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "post/new_post.html"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse("post-detail", kwargs={"post_id": self.object.id})

#post수정
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

#post삭제
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

#comment생성
class CommentCreateView(LoginRequiredMixin, CreateView):
    http_method_names = ['post']
    
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(id=self.kwargs.get('post_id'))
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.kwargs.get('post_id')})

#comment수정
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/comment_update_form.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.post.id})
    
    def test_func(self, user):
        comment = self.get_object()
        return comment.author == user

#comment삭제
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'post/comment_confirm_delete.html'
    pk_url_kwarg = 'comment_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.post.id})
    
    def test_func(self, user):
        comment = self.get_object()
        return comment.author == user

#Like 기능
class ProcessLikeView(LoginRequiredMixin, View):
    http_method_names = ['post']
    
    def post(self, request, *args, **kwargs):
        like, created = Like.objects.get_or_create(
            user=self.request.user,
            content_type_id=self.kwargs.get('content_type_id'),
            object_id=self.kwargs.get('object_id'),
        )       
        if not created:
            like.delete()
        return redirect(self.request.META['HTTP_REFERER'])
    
#Profile 
class ProfileView(LoginRequiredMixin,DetailView):
    model = User
    template_name = "post/profile.html"
    pk_url_kwarg = "user_id"
    context_object_name = "profile_user"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        profile_user_id = self.kwargs.get('user_id')
        if user.is_authenticated:
            context['is_following'] = user.following.filter(id=profile_user_id).exists()
        context["user_post"] = Post.objects.filter(author__id=profile_user_id)[:4]
        return context
    
#Follow 기능 
class ProcessFollowView(LoginRequiredMixin, View):
    http_method_names = ['post']
    
    def post(self, request, *args, **kwargs):
        user = self.request.user
        profile_user_id = self.kwargs.get('user_id')
        if user.following.filter(id=profile_user_id).exists():
            user.following.remove(profile_user_id)
        else:
            user.following.add(profile_user_id)
        return redirect(self.request.META['HTTP_REFERER'], user_id=profile_user_id )

#Following 페이지
class FollowingListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'post/following_list.html'
    context_object_name = 'following'

    def get_queryset(self):
        profile_user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return profile_user.following.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context

#Follower 페이지 
class FollowerListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'post/follower_list.html'
    context_object_name = 'followers'

    def get_queryset(self):
        profile_user = get_object_or_404(User, pk=self.kwargs.get('user_id'))
        return profile_user.followers.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile_user_id'] = self.kwargs.get('user_id')
        return context
    
#팔로우 한 사람만의 list 페이지
class FollowingPostListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {}
        context['latest_posts'] = Post.objects.all()
        user = self.request.user
        if user.is_authenticated:
            context['latest_following_reviews'] = Post.objects.filter(author__followers=user)
        return render(request, 'post/user_post_list.html', context)
    
class FollowingReviewListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'following_posts'
    template_name = 'posts/following_post_list.html'

    def get_queryset(self):
        return Post.objects.filter(author__followers=self.request.user)
    
#profile 설정
class ProfileSetView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "post/profile_set_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("index")

#profile 수정
class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileForm
    template_name = "post/profile_update_form.html"
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse("profile", kwargs=({"user_id": self.request.user.id}))

