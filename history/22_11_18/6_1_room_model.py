python manage.py startapp rooms

# 1. amenity란? (many to many field)
# ㄴ> 방을 보러가면 그 장소가 제공하는 것을 보여준다. model을 만들어서 이런 부엌, 냉장고 같은 컬럼을 만들 건데
# ㄴ> 이걸로 many-to-many 관계 (다대다 관계) 라는 새로운 개념을 알 수 있다.
# 지금 까지는 room에 owner가 있을 때 사용할 Foreign Key만 사용했다.