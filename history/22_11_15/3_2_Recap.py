# Django는 세션, 패스워드, 등 모든 유저 데이터를 저장하는 곳으로 데이터베이스를 사용한다.

"""
You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
"""

# 이 메시지는 DB에 적용되지 않은 마이그레이션 파일이 존재할 때 나타난다.

# Django는 편리하게도 프로젝트를 만들면, 이미 작성된 마이그레이션 파일이 함께 딸려온다.
# 마이그레이션 파일은 데이터베이스의 모양을 변형시키는 파이썬 코드이며 마이그레이션을 적용할 때, 데이터베이스를 변형시키게 되고, 장고는 작업에 필요한 테이블 모두를 갖게 된다.

