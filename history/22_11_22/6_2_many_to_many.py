# 1. many to one 과 one to many의 의미
# ㄴ> 1, 2, 3번방 모두 같은 owner를 가질 수 있다. -> many to one 관계
# ㄴ> 위를 뒤집으면 one to many 관계다. 한 user가 여러 room을 가질 수 있기 때문

# 2. many to many 관계는 여러 amenity 들이 여러 room 안에 있을 수 있도록 해준다
# ㄴ> models.ManyToManyField("rooms.Amenity")

# 3. models.DateTimeField(auto_now_add=True)
# ㄴ> 필드의 값을 해당 object가 처음 생성되었을 때 시간으로 설정한다.
# ㄴ> django가 생성된 시점의 시간(date)를 넣어준다

# 3.1 auto_now_add 와 auto_now 의 차이점
# ㄴ> auto_now_add는 처음 생성되었을 때 date 값이 채워진다.
# ㄴ> auto_now는 django가 업데이트할 때마다 설정된다.
