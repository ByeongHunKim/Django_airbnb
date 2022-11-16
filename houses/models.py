from django.db import models

class House(models.Model):

    """Model Definition for House"""
    
    name = models.CharField(max_length=140)
    # 양수인 정수
    price_per_night = models.PositiveIntegerField()
    # TextField는 CharField보다 길다. CharField는 텍스트를 쓰고 싶을 때 쓰는건데, 길이가 약간 짧거나 문자 길이에 제한을 줘야할 때 쓴다.
    # TextField는 유저가 길이가 긴 텍스트를 쓸 수 있게 해준다. 왜냐면 이것들은 데이터베이스에서 다른 방식으로 표현되기 때문
    description = models.TextField()
    address = models.CharField(max_length=140)
    pets_allowed = models.BooleanField(default=True)

    # admin페이지에서 houses model의 name 컬럼이 렌더링 된다.
    def __str__(self):
        return self.name