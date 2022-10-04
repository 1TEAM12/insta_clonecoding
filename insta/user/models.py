from django.db import models
from django.contrib.auth.models import AbstractUser 
from .validators import validate_no_special_characters #유효성 검사 커스터마이징 import

# Create your models here.
#User model에서 username과 profile_image, intro, following 정의
class User(AbstractUser):
    username = models.CharField(
        max_length=15, #최대 15자
        unique=True, #중복 허용 x
        null=True, #null값 허용
        validators=[validate_no_special_characters], #비밀번호 유효성 검사 
        error_messages={"unique":"이미 사용중인 닉네임입니다."}, #중복일 때 error메시지 뜨게함
        )
    
    profile_image = models.ImageField(
        default="default_profile_pic.jpg",upload_to="profile_pics" 
        )
    
    intro = models.CharField(max_length=60, blank=True)
    
    following = models.ManyToManyField('self', symmetrical=False, blank=True, related_name= 'followers')
    
    def __str__(self):
        return self.email