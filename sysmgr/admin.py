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
    filter_horizontal = ('role',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'pid') # list
    filter_horizontal = ('user', 'role',)


# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Role)
admin.site.disable_action('delete_selected')

