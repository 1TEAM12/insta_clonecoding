from django import forms
from .models import User


class SignupForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["username"]
        
    def signup(self, request, user):
        user.username = self.cleaned_data["username"]
        user.save()