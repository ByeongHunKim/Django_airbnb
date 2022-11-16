from django.contrib import admin
from .models import House

# HouseAdmin이라는 class를 만들고 ModelAdmin class로부터 모든걸 상속받는다.
# HouseAdmin이라는 class가 House model을 통제한다는 의미
@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    # 리스트 출력
    list_display = (
        "name",
        "price_per_night",
        "address",
        "pets_allowed"
    )
    # 필터기능
    list_filter = ("price_per_night", "pets_allowed")
    # 검색기능
    search_fields = ("address",) # ("address__startswith",) : 여기에 들어간 텍스트로 시작하는 것만 검색, endswith, capital or not 도 된다.
    # admin이 수정하지 못하게 함
    exclude = ("price_per_night",)
