"""insta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from user.views import CustomPasswordChangeView

urlpatterns = [
    #admin
    path('admin/', admin.site.urls),
    
    #user
    path('', include('user.urls')),
    
    #post
    path('',include('post.urls')),
    
    #allauth
    path(
        'email-confirmation-required/',
        TemplateView.as_view(template_name='account/email_confirmation_required.html'),
        name='account_email_confirmation_required',
    ),
    
    path(
        'email-confirmation-done/',
        TemplateView.as_view(template_name='account/email_confirmation_done.html'),
        name='account_email_confirmation_done',
    ),
    
    path(
        'confirm-email/',
        TemplateView.as_view(template_name='account/confirm-email.html'),
        name='account_confirm_email',
    ),
    
    path(
            'password/change/',
            CustomPasswordChangeView.as_view(),
            name='account_change_password',
        ),
    
    path('', include('allauth.urls')), #allauth에서 제공하는 url을 커스터마이징 할 때는 항상 url을 allauth보다 위에 작성 url은 위에서 아래로 작동하기 때문
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #media루트 경로를 설정
