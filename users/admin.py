from django.contrib import admin
from .models import Profile, Role
# Register your models here.


class AdminProfile(admin.ModelAdmin):
    pass


class AdminRole (admin.ModelAdmin):
    pass


admin.site.register(Role, AdminRole)
admin.site.register(Profile, AdminProfile)
