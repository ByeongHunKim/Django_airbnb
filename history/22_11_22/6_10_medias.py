# experience, room 모두 많은 양의 사진과 동영상을 가지고 있다.
# 한 개의 방은 많은 사진 또는 동영상을 가질 수 있다.

# 1.models.OneToOneField
# ㄴ> 유저의 결제 정보를 저장할 때 사용할 수 있다.
# ㄴ> 결제 정보 모델을 만들어서 유저랑 연결하는 경우가 생겼을 때 한 명의 유저한테 여러 결제 정보가 생겨서는 안된다.
# ㄴ> 이때 OneToOneField를 사용할 수 있다.

# OneToOneField는 ForeignKey와 같지만 고유한 관계를 생성한다.
# 이 말은 연결된 DB에만 종속된다는 의미이다.
# 하지만 똑같은 활동(experience)에 종속되는 두번째 동영상을 만들 수 없다.
# ForeignKey는 한 개의 방이 많은 사진을 가질 수 있다는 것을 의미한다.

# ORM -> DB에서 데이터를 가져오는 방법
