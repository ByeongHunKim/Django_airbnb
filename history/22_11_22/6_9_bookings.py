# 1명의 유저는 많은 예약을 가질 수 있지만, 예약은 오직 한 명의 유저밖에 가질 수 없다.

# 한 개의 예약이 많은 방을 가질 수 있을까? -> 한 개의 방은 많은 예약을 가질 수 있다.

"""
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField()
"""

# ㄴ> room 예약일수도 있고, experience 예약일 수 있다. 그래서 null=True, blank=True 옵션을 줘서 필수값이 아니어도 되도록 설정
