from django.db import models


class User(models.Model):
    email = models.EmailField('이메일', unique=True)
    name = models.CharField('이름', max_length=150, null=True)