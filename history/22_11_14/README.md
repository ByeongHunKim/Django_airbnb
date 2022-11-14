# poetry 명령어

- poetry init
- poetry add django
- poetry shell (가상환경 활성화)
  - exit (가상환경 비활성화)

# django 명령어

- django-admin startproject config .
  - 명령어를 실행시킨 디렉토리 위치에서 config/ , manage.py 파일 생성됨

# TIPS

- gitignore (CodeZombie) extention 설치
  - settings -> command palette 에서 add gitignore 선택 후 python 언어 선택하면 알아서 세팅된다.

```
☁  django_airbnb [main] ⚡  poetry init

This command will guide you through creating your pyproject.toml config.

Package name [django_airbnb]:
Version [0.1.0]:
Description []:
Author [ByeongHunKim <rkwhr912@naver.com>, n to skip]:
License []:  MIT
Compatible Python versions [^3.8]:

Would you like to define your main dependencies interactively? (yes/no) [yes] no
Would you like to define your development dependencies interactively? (yes/no) [yes] no
Generated file

[tool.poetry]
name = "django-airbnb"
version = "0.1.0"
description = ""
authors = ["ByeongHunKim <rkwhr912@naver.com>"]
license = "MIT"
readme = "README.md"
packages = [{include = "django_airbnb"}]

[tool.poetry.dependencies]
python = "^3.8"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] yes

☁  django_airbnb [main] ⚡  poetry add django
Creating virtualenv django-airbnb-7f8lxYnd-py3.8 in /home/bstudent/.cache/pypoetry/virtualenvs
Using version ^4.1.3 for Django

Updating dependencies
Resolving dependencies... (0.4s)

Writing lock file

Package operations: 4 installs, 0 updates, 0 removals

  • Installing asgiref (3.5.2)
  • Installing backports-zoneinfo (0.2.1)
  • Installing sqlparse (0.4.3)
  • Installing django (4.1.3)
```
