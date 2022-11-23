# .all(), .get(), .filter(), .create(), .delete()를 배웠다.
 

# object 객체를 통한 반복문
"""
from rooms.models import Room
Room.objects.all()

for room in Room.objects.all():
    print(room.name)

output -> 모든 name 출력
"""

# .get()
# ㄴ> .get()은 단 하나의 model, 단 하나의 데이터만 반환할 수 있다. 만약 다수의 objects 가 반환되는 경우는 에러가 남
# ㄴ> 그래서 "특별한 무언가"를 찾고싶을 때 쓰인다.

# .filter()
# .get()에서는 다수의 objects가 반환되는 경우 에러가 났지만, filter()는 에러가 나지 않는다.
# Django ORM의 멋있는 점은 , filter 메서드가 정말 강력하다는 것
# ex) 하루 숙박비가 15$가 넘은 room들을 찾고싶은 경우에 True,False냐 같은 것만을 찾으려고 매달리지 않아도 된다.
#     ㄴ> Room.objects.filter(price__gt==15)
# gte : greater than equal (이상)
# lte : less than equal (이하)

기타 Lookup 예시들을 통해 Django로 얼마나 강력한 기능을 쓸 수 있는지 알 수 있다.
# .filter(name__contains="blahblah")

# .filter(name__startswith="blahblah")


# .create()
"""
from rooms.models import Amenity
Amenity.objects.all()

Amenity.objects.create() -> 아무것도 없는게 생성된다.

()안의 속성들은 실제로 해당 model에 존재하는 컬럼들이어야 한다
Amenity.objects.create(name="example", description="test create")
"""

# .delete()를 통해 id가 7번인 것 삭제하기 
"""
to_delete = Amenity.object.get(pk=7)
to_delete.delete() -> 삭제
"""
