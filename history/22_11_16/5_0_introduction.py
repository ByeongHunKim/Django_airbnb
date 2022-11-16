# 사용자의 프로필 이미지가 있으면 좋겠는 경우, Django의 User모델은 프로필 이미지를 지원하고 있지 않다.
# 또는 사용자가 비밀번호로 로그인하는 방식이 아닌 소셜 네트워크로 로그인하는 걸 원하는 방식일 수도 있다.
# 그러면 User의 구성을 조금 커스텀 하는 게 필요하다. ( 우리만의 User 모델로 아예 교체하는 방식 ) -> 그래서 Django application을 시작하는 처음부터 userModel을 교체해야한다.

# 익스텐션 설치 : pylance
# 라이브러리 설치 : black

"""
    ~/p/Django_airbnb    main ?1  poetry add --dev black --allow-prereleases
The --dev option is deprecated, use the `--group dev` notation instead.
Using version ^22.10.0 for black

Updating dependencies
Resolving dependencies... (0.8s)

Writing lock file

Package operations: 7 installs, 0 updates, 0 removals

  • Installing click (8.1.3)
  • Installing mypy-extensions (0.4.3)
  • Installing pathspec (0.10.2)
  • Installing platformdirs (2.5.4)
  • Installing tomli (2.0.1)
  • Installing typing-extensions (4.4.0)
  • Installing black (22.10.0)
"""
