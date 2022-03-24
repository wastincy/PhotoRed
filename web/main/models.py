from django.db import models

class User(models.Model):
    id = models.CharField('id', primary_key=True, max_length=10)
    login = models.CharField('login', max_length=30)
    password = models.CharField('password', max_length=30)

    def __str__(self):
        return self.title

