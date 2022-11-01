from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'username',
        'is_superuser'
    )
    list_display_links = (
        'id',
        'name',
        'username',
    )
    readonly_fields = (
        'password',
    )

admin.site.register(models.User, UserAdmin)