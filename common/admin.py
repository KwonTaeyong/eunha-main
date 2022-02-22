from django.contrib import admin

from .models import User

# Register your models here.

class User_admin(admin.ModelAdmin):
    search_fields = ['username']


admin.site.register(User, User_admin)