from django.db import models
from django.contrib.auth.models import AbstractUser

"""
AbstractBaseUser 구성
- password
- last_login (선택)

AbstractUser 구성 [AbstractBaseUser 상속]
- username
- first_name (선택)
- last_name (선택)
- email (선택)
...

*참고자료: https://han-py.tistory.com/144
"""


# 기존 AbstractUser 모델에 새로운 필드 추가
class User(AbstractUser):
    phone = models.CharField(max_length=20)
    snu_mail = models.CharField(max_length=100)

