from django.contrib import admin
from forms import UserForm
from sysmgr import models

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    form = UserForm
    list_display = ('login_name', 'username', 'is_active') # list
    list_filter = (
            ('is_active', admin.BooleanFieldListFilter),
            )

admin.site.register(models.User, UserAdmin)

# Register your models here.
