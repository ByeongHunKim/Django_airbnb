# model을 연결하는 방법
# ㄴ> 데이터베이스에 이 연결성을 어떻게 표현할 수 있는가?

# Django랑 데이터베이스는 기본적으로 unique한 ID를 데이터베이스에 있는 모든 object에 만들고 있다.
# 그래서 원하든 않든 데이터베이스에 생성된 모든 것들은 ID를 가지고 있다.
# Django에서는 이 ID를 라고 부르지 않고 PK(Primary Key)라고  부른다.
# Foreign key 타입을 사용하면 Django는 단순히 숫자가 아니라는 것을 안다
# ㄴ> 해당 숫자가 users 데이터베이스에 있는 user의 ID라는 걸 알게된다.

1. owner = models.ForeignKey("users.User")
# 어떤 model의 reference(참조)를 저장하는 지 알려줘야한다.

2. TypeError: __init__() missing 1 required positional argument: 'on_delete'
# Foreign Key도 필수 요소로 on_delete가 필요하다.
# ㄴ> on_delete는 참조하는 model이 삭제될 때 어떻게 할건지를 설정하게 해준다
# 그래서 연결된 model이 삭제될 때 어떻게 할지 특정할 수 있다

3. owner = models.ForeignKey("users.User", on_delete=models.SET_NULL)
# 연결된 model이 삭제되면 Null로 바꿈

4. owner = models.ForeignKey("users.User", on_delete=models.CASCADE)
# CASCADE의 의미는 만약에 사용자가 지우면 연결된 model도 지워진다
