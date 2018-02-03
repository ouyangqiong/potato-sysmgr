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

class RoleMenuInline(admin.TabularInline):
    model = models.RoleMenuPermission
    extra = 0

class RoleRegionInline(admin.TabularInline):
    model = models.RoleRegionPermission
    extra = 0

class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc') # list
    inlines = (RoleMenuInline, RoleRegionInline, )

class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'pid', 'menu_type', 'code', 'name',
        'desc', 'addr', 'addr_param', 'i_class', 'sort', 'is_active')
    search_fields = ("code", "name",)
    list_filter = ('menu_type',)

class RegionAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc') # list
    filter_horizontal = ('menu',)

class RegionInline(admin.TabularInline):
    model = models.Region
    extra = 0

class ProviderAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'desc') # list
    inlines = (RegionInline, )



# Register your models here.
admin.site.register(models.User, UserAdmin)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.Menu, MenuAdmin)
admin.site.register(models.Region, RegionAdmin)
admin.site.register(models.Provider, ProviderAdmin)
admin.site.disable_action('delete_selected')

