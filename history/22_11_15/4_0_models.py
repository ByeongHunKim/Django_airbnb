# python manage.py startapp houses

"""
houses/models.py에 # Create your models here. 라고 말하고 있듯이 여기가 데이터의 모양을 Django에게 알려줘야하는 곳 이다.
모델은 어플리케이션에서 데이터의 모양을 묘사한 것이다. 그래서 우리의 경우 house를 만들었다.
house는 주소, 설명, 일박 가격, 사진, 이름등 이 모든 것들이 데이터에 대한 설명이다.
그래서 데이터를 설명하고, 그 데이터가 어떤 종류인지 알려줘야한다.

집, 경험, 하우스 규칙, 편의시설을 위한 모델, 예약, 유저, 리뷰, 리스트를 위한 모델, 메시지를 위한 모델 등등 너무나 다양하다
"""

from django.db import models

class House(models.Model):

    """Model Definition for House"""
    
    name = models.CharField(max_lentgh=140)
    # 양수인 정수
    price = models.PositiveIntegerField()
    # TextField는 CharField보다 길다. CharField는 텍스트를 쓰고 싶을 때 쓰는건데, 길이가 약간 짧거나 문자 길이에 제한을 줘야할 때 쓴다.
    # TextField는 유저가 길이가 긴 텍스트를 쓸 수 있게 해준다. 왜냐면 이것들은 데이터베이스에서 다른 방식으로 표현되기 때문
    description = models.TextField()
    address = models.CharField(max_length=140)

# 이렇게 새로운 application의 models.py를 설정해줘도 서버가 재시작되지 않는 이유는 Django가 아직 해당 application(python manage.py startapp houses)에 대해 알지 못하기 때문이다.

# config/settings.py 에서 INSTALLED_APPS 에 우리가 갖고 있는 어플리케이션을 알려줘야한다.

