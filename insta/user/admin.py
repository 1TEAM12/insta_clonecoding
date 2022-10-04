from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

admin.site.register(User, UserAdmin)

class UserInline(admin.StackedInline):
    model = User.following.through
    fk_name = 'to_user'
    verbose_name = 'Follower'
    verbose_name_plural = 'Followers'
    
UserAdmin.fieldsets += (("Profile fields", {"fields": ("profile_image", "intro", "following")}),) #Admin Field 커스터마이징
UserAdmin.inlines = (UserInline,)

