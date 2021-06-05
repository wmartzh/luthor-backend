from django.db import models

# Create your models here.


class Assistance(models.Model):

    class Meta:
        verbose_name = ("Assistance")
        verbose_name_plural = ("Assistance")

    def __str__(self):
        return self.name
