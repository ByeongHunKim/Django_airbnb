from django.contrib import admin
from .models import House

# HouseAdmin이라는 class를 만들고 ModelAdmin class로부터 모든걸 상속받는다.
# HouseAdmin이라는 class가 House model을 통제한다는 의미
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    pass