"""
Django settings for insta project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = # 

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites', 
    'user',
    'post',
    'widget_tweaks', #템플릿 변수의 속성값을 쉽게 정의
    'allauth',
    'allauth.account',
    'allauth.socialaccount', #소셜로그인
    'allauth.socialaccount.providers.kakao', #카카오 소셜로그인
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'post.middleware.ProfileSetupMiddleware',
 ] #request가 아래에서 위로 response가 위에서 아래로 페이지를 접근할 때 반드시 거쳐야 하는 로직

SITE_ID = 1

ROOT_URLCONF = 'insta.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'insta.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'user.validators.CustomPasswordValidator',
    }
] #비밀번호 유효성 검사할 때 커스터마이징한 비밀번호로 사용하겠다는 뜻


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ko'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
BASE_DIR/'static',
] #static 경로를 프로젝트폴더와 동일 선상으로 Base

STATIC_URL = 'static/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  #이미지 저장되는 경로는 media로 베이스 설정
MEDIA_URL = '/uploads/' #미디어 경로를 http://127.0.0.1:8000/uploads/....

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

#Auth settings
AUTH_USER_MODEL = "user.User" #allauth는 model을 제공해주지 않기에 User모델을 가져옴

#allauth 기본 세팅
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
] 

ACCOUNT_SIGNUP_REDIRECT_URL = "account_login" #회원가입하면 어디로 redirect할지 정의
LOGIN_REDIRECT_URL = "index"  #로그인하면 어디로 redirect할지 정의
LOGIN_URL = "account_login" #Login url 정의 
ACCOUNT_LOGOUT_ON_GET = True #logout 페이지를 거치지 않고 바로 Logout 되게함 (기본값 False)
ACCOUNT_AUTHENTICATION_METHOD = "email" # 로그인시 username 이 아니라 email을 사용하게 하는 설정(기본값 username)
ACCOUNT_EMAIL_REQUIRED = True  ## 회원가입시 필수 이메일을 필수항목으로 만들기 (기본값 False)
ACCOUNT_SESSION_REMEMBER = True #브라우저를 나가더라도 브라우저가 자동으로 session을 저장하도록 (기본값 False)
SESSION_COOKIE_AGE = 3600 #로그인 후 session cookie의 지속시간 (기본값 2주/초단위) 
ACCOUNT_SIGNUP_FORM_CLASS = "user.forms.SignupForm" #기존의 signup form을 쓰지않고 커스터 마이징한 form을 가져다 씀 
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True  #비밀번호가 틀리면 새로고침되면서 초기화 되는 값을 저장하게함(기본값 False)
ACCOUNT_EMAIL_VERIFICATION = "mandatory" #이메일 인증은 반드시 하도록(기본값 optional)
ACCOUNT_CONFIRM_EMAIL_ON_GET = True # 유저가 받은 링크를 클릭하면 회원가입 완료되게끔 (기본값 False)
ACCOUNT_EMAIL_CONFIRMATION_AUTHENTICATED_REDIRECT_URL ="account_email_confirmation_done" #이메일 인증이 완료되었을 때 어디로 리디렉트 되게할지(로그인인 상태)
ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL = "account_email_confirmation_done" #이메일 인증이 완료되었을 때 어디로 리디렉트 되게할지(로그아웃인 상태)


#Email settings
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend" #기본값으로 설정되어있음
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend" #일단 console로 돌리기 위해서 설정
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
# EMAIL_HOST_USER = "보낼 이메일 주소"
# EMAIL_HOST_PASSWORD = "app 비밀번호"
