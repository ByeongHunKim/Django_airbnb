# 객체를 생성하고, 찾아오고, 갱신하고, 삭제할 수 있게한다.

# python manage.py shell
# ㄴ>

"""
from rooms.models import Room
Room.objects
ㄴ> Room class에 objects 속성을 준다.
ㄴ> objects 속성은 수많은 메소드를 가지고 있는데, 이 메소드들을 이용하면 데이터베이스가 Room 모델에서 나온 데이터들을 꺼내오도록 시킬 수 있다.
"""

# 어떤 메서드들이 있을까?
Room.objects.all() : 해당 모델의 모든 데이터를 가져온다

Room.objects.get() : 해당 모델에 있는 어떤 속성이라도 찾아올 수 있다
ex) Room.objects.get(name="blah,blah")

.create()
.filter()



# 예시코드-----------------------------------------------------------------------------------------------------------------------
from rooms.models import Room

room = Room.objects.get(name="adb")

room.pk 
# output : "abd"라는 name 컬럼을 가진 유저의 PK가 나온다.

room.name
# 이렇게 해당 모델의 모든 속성 하나하나를 호출하던지 변수에 저장할 수 있다.

room.owner.email
# owner가 PK 데이터타입이어서 그 owner의 email 값을 확인할 수 있다.

# price 속성을 변경하는 방법
room.price
# output : 1
room.price = 20
room.save()
room.price
# output : 20
# price 속성을 변경하는 방법



# 예시코드-----------------------------------------------------------------------------------------------------------------------
