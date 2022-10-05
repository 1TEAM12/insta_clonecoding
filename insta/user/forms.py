from django import forms
from django.contrib.auth.hashers import check_password
from .models import User


# Form의 username 작성
class SignupForm(forms.ModelForm):

    class Meta:
        model = User 
        fields = ["username"]  
        
    def signup(self, request, user):
        user.username = self.cleaned_data["username"] #
        user.save()
        

# 회원 탈퇴를 위한 패스워드 Check Form
class CheckPasswordForm(forms.Form):
    password = forms.CharField(label='비밀번호', widget=forms.PasswordInput(
        attrs={'class': 'form-control',}), 
    )
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = self.user.password
        
        if password:
            if not check_password(password, confirm_password):
                self.add_error('password', '비밀번호가 일치하지 않습니다.')