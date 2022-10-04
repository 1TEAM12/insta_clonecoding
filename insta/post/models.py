from django.db import models
from user.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to="post_pics")
    content = models.TextField(max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    
    likes = GenericRelation('Like', related_query_name ='post')
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-created_at']

class Comment(models.Model):
    content = models.TextField(max_length=50, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE,  related_name='comments')
    
    likes = GenericRelation('Like', related_query_name ='post')
    
    def __str__(self):
        return self.content[:30]
    
    class Meta:
        ordering = ['-created_at']
    
class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='likes')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    
    object_id = models.PositiveIntegerField()
    
    liked_object = GenericForeignKey()
    
    def __str__(self):
        return f"({self.user},{self.liked_object})"