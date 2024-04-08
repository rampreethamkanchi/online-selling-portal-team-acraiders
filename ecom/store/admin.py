from django.contrib import admin
from .models import Category,Customer,Product,Order,Address,Request,Manager,Chat,User,Issue
from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(Request)
admin.site.register(Manager)
admin.site.register(Chat)
admin.site.register(Issue)


# class UserAdmin(BaseUserAdmin):
# form = UserChangeForm
# fieldsets = (
# 	(None, {'fields': ('email', 'password', )}),
# 	(_('Personal info'), {'fields': ('first_name', 'last_name')}),
# 	(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
# 									'groups', 'user_permissions')}),
# 	(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
# 		(_('user_info'), {'fields': ('native_name', 'phone_no')}),
# )
# add_fieldsets = (
# 	(None, {
# 		'classes': ('wide', ),
# 		'fields': ('email', 'password1', 'password2'),
# 	}),
# )
# list_display = ['email', 'first_name', 'last_name', 'is_staff', "native_name", "phone_no"]
# search_fields = ('email', 'first_name', 'last_name')
# ordering = ('email', )
# admin.site.register(User, UserAdmin)
