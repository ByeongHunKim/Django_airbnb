# Django에게 왜 이런 식으로 데이터를 설명해야 하는지를 알아볼 것
# 이유 중 하나는 Django가 DB와 소통해야하기 때문. 데이터베이스는 파이썬 코드로 소통하지 않는다. (SQL코드)

# houses/models.py에서 데이터베이스에 대해서 정의를 해줬고, Django가 houses라는 application을 알고 있다는 걸 설정해주기 위해
# config/settings.py에서 INSTALLED_APP에서 설정도 해주었다. 하지만 migration을 해주지 않았기 때문에 데이터베이스는 House model에 대해서 전혀 모르는 상태다.

# 무엇이 데이터베이스의 형태를 수정할까? 그 정답은 migration!

"""
   ~/p/Django_airbnb    main !1 ?1  python manage.py makemigrations

Migrations for 'houses':
  houses/migrations/0001_initial.py
    - Create model House
"""

# Django가 houses/migrations 라는 폴더 내부에 파일을 만들었다.
# 이렇게 Django가 migration을 만들어냈고, 이 migration을 적용시키면 데이터베이스의 상태가 변경될 것
# python manage.py makemigrations 을 통해 생성된 migration이 있으니 적용시키면 된다.

"""
    ~/p/Django_airbnb    main !1 ?2  python manage.py migrate      ✔  django-airbnb-w705VANB-py3.8   17:08:31 

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, houses, sessions
Running migrations:
  Applying houses.0001_initial... OK
"""

# python manage.py migrate 을 하지 않고 runserver를 하면 장고가 아직 migrations 내부에 적용되지 않은 파일이 있다는 것을 알려준다. (3_2 참조)