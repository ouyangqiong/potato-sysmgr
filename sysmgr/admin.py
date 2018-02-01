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


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'pid') # list


# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Group)

