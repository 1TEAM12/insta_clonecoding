from django import forms
from .models import Post
from user.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "image",
            "content",
        ]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "profile_image",
            "intro",
        ]
        widgets = {
            "intro": forms.Textarea,
        }