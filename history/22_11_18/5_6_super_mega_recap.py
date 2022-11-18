# 1. SQL 같은 관계형 DB와 Django에서의 연결성

# Django는 해당 컬럼을 데이터베이스에 추가해서 null로 둘 수 있다.
null = True

# Charfield는 null이 안된다.
default = ""

# booleanField는 null이 안된다.
default = False / True

# 파이썬 코드와 데이터베이스의 구조는 동기화 되어야 한다.
# 왜냐하면 파이썬 코드는 같은 형태에 있을 때만 데이터베이스랑 소통하기 때문.

# --------------------------------------------------------------------------------------------

# 2. 관계(relationship)

# ex) houses application <-> users application을 연결시키고 싶은 경우 (owner가 house를 가지기 때문에 house에 주인이 필요함) -> (owner가 지갑을 가지기 때문에 지갑에 주인이 필요함)
# 서로 다른 model은 다른 테이블에 있다.

# 관계형 데이터베이스는 자동으로 데이터에 ID를 부여한다
# 그래서 사용자 데이터를 복사하는 것 대신에 사용자의 ID를 저장
# model 설정해줄 때 Primary Key 즉, ID를 참조한다고 코드를 명시해주면 된다.

owner = models.ForeignKey("users.User", on_delete=models.CASCADE)

# ForeignKey field는 두 개의 요소가 필요하다
# ㄴ> 1. model의 이름과 그걸가지고 있는 application의 이름
# ㄴ> 2. on_delete : house의 주인 user가 계정을 지우면 어떻게 할 지 설정하게 해준다.
# ㄴ> 함께 삭제되거나, default값을 설정할 수도 있고, 어떻때는 null=True를 추가할 수 있다

# CASCADE
# ㄴ> 이번 케이스에는 주인없는 house를 가지는 것이 말이 안되기 때문에 함께 삭제되는 models.CASCADE를 넣었다

# SET_NULL
# ㄴ> 하지만 결제정보라던지, 이렇게 사용자가 계정을 지워도 관련 내역을 삭제하고 싶지 않다면, models.SET_NULL
# ㄴ> 그러면 유저가 계정을 삭제했을 때 해당 ID 값만 NULL로 변하면서 주인이 없어지게 된다. 하지만 데이터는 남아있음
# ㄴ> 어떨 때는 연결된 사용자가 계정을 지워도 기록을 유지하고 싶을 수 있는 상황이 있을 수 있으니 고려해야한다


# 아직 model 생성이나 관리자 페이지를 생성하고 커스텀하는게 쉽지 않을 것..
# #6 MODELS AND ADMIN 에서 많이 연습할 것
