from django.shortcuts import render, redirect
from django.urls import reverse
from braces.views import LoginRequiredMixin 
from allauth.account.views import PasswordChangeView 
from django.contrib.auth.hashers import check_password

# Create your views here.

#비밀번호 유효성 검사
class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self): #get_success_url이라는 것은 어디로 리디렉스해줄지 정해주는 것
        return reverse("profile", kwargs={"user_id":self.request.user.id })




# 계정 삭제
def account_delete(request):
    if request.method == "POST":
        pw_del = request.POST['pw_del']
        user = request.user
        if check_password(pw_del, user.password):
            user.delete()
            return redirect('/')
    return render(request, 'account/account_delete.html')