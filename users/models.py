from django.db import models
from dorms.models import Dorm
from django.contrib.auth import get_user_model
User = get_user_model()


class Role(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


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
