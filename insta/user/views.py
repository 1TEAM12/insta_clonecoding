from django.shortcuts import render
from django.urls import reverse
from braces.views import LoginRequiredMixin
from allauth.account.views import PasswordChangeView

# Create your views here.

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    def get_success_url(self):
        return reverse("profile", kwargs={"user_id":self.request.user.id })
    
