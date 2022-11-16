from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# 이 class가 user model을 관리한다고 명시
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    pass
