# .all() 이나 .filter()를 호출할 때마다 return 값으로 querySet을 받았다.

# querySet이란 무엇인가?
# ㄴ> 연산자를 함께 묶어주는일을 한다.

# exclude : lookup 매개변수(lte, lt, gt, gte) 와 일치하지 않는 objects를 포함한 QuerySet을 반환한다.
# ex)
#     Room.objects.filter(pet_friendly=True).exclude(price__lt=15).filter(name__contains="서울")
# 이렇게 각각의 filter를 연결할 수 있다. 포함할 수 있는 건 포함하고, 제외할 수 있는 건 제외하고 있다.
# 하지만 이건 좀 비효율적인 예시코드다. 이 모든 걸 한번에 진행할 수 있는 filter가 있다.

# Room.objects.filter(pet_friendly=True, name__contains="서울", price__gt=15)

# Room.objects.filter(pet_friendly=True).count()
