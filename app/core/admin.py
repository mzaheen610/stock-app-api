"""
Admin site for the stocks api.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from core import models


class UserAdmin(BaseUserAdmin):
    """Define admin page for the users"""
    ordering = ['id']
    list_display = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Permissions'),
         {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                )
            }
        ),
        (_('Important Dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )


class StockAdmin(admin.ModelAdmin):
    """Admin for the stocks model"""
    empty_value_display = "-empty-"
    ordering = ['name']
    list_display = ['name', 'price', 'user']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Stock, StockAdmin)
