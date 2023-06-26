from django.contrib import admin
from .models import User
from .models import School

admin.site.register(School)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'password')
