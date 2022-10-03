from django.urls import path
from . import views

urlpatterns = [
    #post urls
    path('', views.IndexView.as_view(), name="index"),
    path(
        'post/<int:post_id>/',
        views.PostDetailView.as_view(),
        name="post-detail"
    ),
    path(
        'post/new/',
        views.PostCreateView.as_view(), 
        name="post-create"
    ),
    path(
        "post/<int:post_id>/edit/",
        views.PostUpdateView.as_view(),
        name="post-update",
    ),
    path(
        "post/<int:post_id>/delete/",
        views.PostDeleteView.as_view(),
        name="post-delete",
    ),
    
    #profile urls
    path("users/<int:user_id>/", views.ProfileView.as_view(), name="profile"),
    path("set-profile/",views.ProfileSetView.as_view(), name="profile-set"),
    path("edit-profile/",views.ProfileUpdateView.as_view(), name="profile-update"),
]