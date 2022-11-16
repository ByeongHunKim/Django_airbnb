# admin 패널에 어떻게 column 들을 구현하는가? 
# reference : list_display property

# 중요한 것은 대괄호 [] 대신에 괄호() 튜플 를 자주 쓴다.
# 만약 튜플에 한 개의 element 밖에 없어도 tuple로 유지되게 하려면 콤마를 붙여주면 된다.

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

# 특정 컬럼들을 선택해서 삭제하는 액션만 있는게 아니라 여기에 추가적인 동작들을 만들 수 있다.
# 그러면 admin 페이지에서 배송 후 리워드 신청에 대한 데이터들이 쌓이는 DB에 admin이 선택한 후 전송 버튼을 누르면? web3 함수에 해당 데이터를 블록에 태워서 트랜잭션을 발생시키고, waitTransaction으로 pending이 완료되면 나머지 status(BooleanField), hash(charField)에 값을 넣어주고 save()
# 나중에 윗줄처럼 구현이 되면, goerli testnet으로 해보면 되겠다. ETH로만 우선.. 