from django.contrib import admin
from .models import Post, Comment, Like
from django.contrib.contenttypes.admin import GenericStackedInline

# Register your models here.

#inline(같은 줄에)
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

#Post와 PostAdmin에 등록
admin.site.register(Post, PostAdmin)

#Comment와 Commentadmin admin에 등록
admin.site.register(Comment, CommentAdmin)

#like admin에 등록
admin.site.register(Like)

#Bookmark admin에 등록
# admin.site.register(Bookmark)
