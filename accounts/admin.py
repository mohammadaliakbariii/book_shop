from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import User
# Register your models here.



class AccountAdmin(UserAdmin):
    list_display = ("email","full_name","date_joined","last_login","is_superuser","is_admin","is_staff","is_active",)
    search_fields = ('email',)
    readonly_fields = ('id','date_joined','last_login',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',"full_name","is_superuser","is_admin","is_staff","is_active", 'password1', 'password2',),
        }),
    )


admin.site.register(User,AccountAdmin)
