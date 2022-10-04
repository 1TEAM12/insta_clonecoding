from django import forms
from .models import Post, Comment
from user.models import User

#PostForm
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "image",
            "content",
        ]

#ProfileForm
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "username",
            "profile_image",
            "intro",
        ]
        widgets = {
            "intro": forms.Textarea,
        }

#Form
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        
        widgets = {
            'content': forms.TextInput,
        }
# (attrs={'class': ''}) 뒤에 갖다붙일 수도 있음 지우지말것