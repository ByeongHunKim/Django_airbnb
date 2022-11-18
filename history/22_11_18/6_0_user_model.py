# 1. imageField
# ㄴ> pillow 를 설치하지 않으면 사용 불가능
# ㄴ> pillow ( python에서 이미지를 가지고 작업할 수 있게 해주는 패키지 )

"""
    ~/p/Django_airbnb    main  poetry add pillow           ✔  22s   django-airbnb-w705VANB-py3.8   09:47:44 
Using version ^9.3.0 for pillow

Updating dependencies
Resolving dependencies... (0.2s)

Writing lock file

Package operations: 1 install, 0 updates, 0 removals

  • Installing pillow (9.3.0)

"""

# 2.form에서 avatar를 필수가 아니게 하려면 models.py에서 해당 컬럼 속성에 blank=True 로 해주면 된다.

# blank=True는 form에서 필드가 필수적이지 않게 해준다. -> 단지 form에서 필드를 비워둘 수 있다고 하는 것
# null=True는 데이터베이스에서 필드가 null 값을 가질 수 있게 해준다.
