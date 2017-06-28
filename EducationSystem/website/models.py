from django.db import models
from django.utils.translation import ugettext_lazy as _


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(_('password'), max_length=128)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    last_login = models.DateTimeField(_('last login'), blank=True, null=True)

    @classmethod
    def login(cls, email, password):
        try:
            u = cls.objects.get(email=email, password=password)
            return u
        except cls.DoesNotExist:
            return None

    @classmethod
    def exists(cls, email):
        try:
            u = cls.objects.get(email=email)
            return True
        except cls.DoesNotExist:
            return False

    def __str__(self):
        return self.email


class Course(models.Model):
    description = models.CharField(max_length=10)

