from django.shortcuts import render
from django.urls import reverse
from braces.views import LoginRequiredMixin 
from allauth.account.views import PasswordChangeView 

# Create your views here.

#비밀번호 유효성 검사
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self): #get_success_url이라는 것은 어디로 리디렉스해줄지 정해주는 것
        return reverse("profile", kwargs={"user_id":self.request.user.id })
