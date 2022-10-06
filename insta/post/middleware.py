from django.urls import reverse
from django.shortcuts import redirect

#항상 회원가입을 하고 난 뒤에 Profile설정을 하도록 설정(이것을 항상 거치도록!)
class ProfileSetupMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if (
            request.user.is_authenticated
            and not request.user.intro
            and request.path_info != reverse("profile-set")
        ):
            return redirect("profile-set")
        
        response = self.get_response(request)
        
        return response
