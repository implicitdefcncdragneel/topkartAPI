from django.contrib import admin
from api.account.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("email","user_role")

admin.site.register(User,UserAdmin)