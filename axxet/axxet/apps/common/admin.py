from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Organization

# Define an inline admin descriptor for Organization model
# which acts a bit like a singleton


class OrganizationInline(admin.StackedInline):
    model = Organization
    can_delete = False
    verbose_name_plural = 'organization'

# Define a new User admin


class UserAdmin(UserAdmin):
    inlines = (OrganizationInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
