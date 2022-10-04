from django import forms
from .models import User

# Form의 username 작성
class SignupForm(forms.ModelForm):

    class Meta:
        model = User 
        fields = ["username"]  
        
    def signup(self, request, user):
        user.username = self.cleaned_data["username"] #
        user.save()