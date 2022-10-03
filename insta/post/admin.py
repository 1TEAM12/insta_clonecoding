from django.contrib import admin
from .models import Post, Comment, Like
from django.contrib.contenttypes.admin import GenericStackedInline
# Register your models here.


class CommentInlie(admin.StackedInline):
    model = Comment

class LikeInlie(GenericStackedInline):
    model = Like
    
class PostAdmin(admin.ModelAdmin):
    inlines = (
        CommentInlie,
        LikeInlie,
    )

class CommentAdmin(admin.ModelAdmin):
    inlines = (
        LikeInlie,
    )
    
admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)

admin.site.register(Like)
