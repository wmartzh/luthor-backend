from django.db import models
from dorms.models import Dorm


class Role(models.Model):
    name = models.CharField(max_length=120)


class User(models.Model):
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    timestamp = models.DateField(auto_now=True)


class Profile(models.Model):
    STATUSES = (
        ('in', 'in'),
        ('out', 'out'),
        ('penalized', 'penalized')
    )

    code = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    status = models.CharField(max_length=50, choices=STATUSES)
    is_active = models.BooleanField(default=False)
    dorm = models.ForeignKey(Dorm, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
