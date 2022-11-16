# AbstractUser를 상속 받은 뒤, 기본적으로 제공되는 컬럼 중 firstname, last name을 가지는 것이 서양적이기 때문에 사용자가 이름만 사용하게 하려면?
# ㄴ> 원치않는 필드를 유령 필드로 만들면 된다.
# ㄴ> editable을 설정하면 관리자 페이지에 나타나지 않는다.

"""
    ~/p/Django_airbnb    main  python manage.py makemigrations
It is impossible to add a non-nullable field 'name' to user without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option:
"""
# ㄴ> 데이터베이스는 기존 행에 입력 시킬 데이터가 필요하기 때문. 2 선택!
