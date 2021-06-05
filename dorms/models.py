from django.db import models

# Create your models here.


class Dorm(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Dorm")
        verbose_name_plural = ("Dorms")

    def __str__(self):
        return self.name
