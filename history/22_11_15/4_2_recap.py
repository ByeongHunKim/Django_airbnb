# Django 에서 application은 데이터와 그 데이터의 로직이 있는 섬 같은 것

# application들을 따로 두고 싶으면 settings.py 에서 설정을 변경해주면 된다.

CUSTOM_APPS = [
    'houses.apps.HousesConfig',
]

SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = SYSTEM_APPS + CUSTOM_APPS

"""
    ~/p/Django_airbnb    main !2 ?1  python manage.py makemigrations
Was house.price renamed to house.price_per_night (a PositiveIntegerField)? [y/N] y
Migrations for 'houses':
  houses/migrations/0002_rename_price_house_price_per_night_and_more.py
    - Rename field price on house to price_per_night
    - Add field pets_allowed to house

    ~/p/Django_airbnb    main !2 ?2  python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, houses, sessions
Running migrations:
  Applying houses.0002_rename_price_house_price_per_night_and_more... OK
"""

