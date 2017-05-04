from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin_
from django.utils.translation import ugettext as _

from .models import (
    User, Subject, Interest, Relationship, Message
)
from .forms import UserSignupForm, UserChangeForm


class UserAdmin(UserAdmin_):
    list_display = ('email', 'full_name', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': ('full_name',)}),
        (_('Permissions'), {'fields': (
            'is_active', 'is_verified', 'is_staff',
            'is_superuser', 'groups', 'user_permissions'
        )}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password'),
        }),
    )
    form = UserChangeForm
    add_form = UserSignupForm


admin.site.register(User, UserAdmin)


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Subject, SubjectAdmin)


class InterestAdmin(admin.ModelAdmin):
    list_display = ('user', 'subject', 'iam', 'level',)
    search_fields = ('user', 'subject', 'iam', 'level',)


admin.site.register(Interest, InterestAdmin)


class RelationshipAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student', 'learn', 'teach',)
    search_fields = ('teacher', 'student', 'learn', 'teach',)


admin.site.register(Relationship, RelationshipAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'created_at')
    search_fields = ('sender', 'receiver')


admin.site.register(Message, MessageAdmin)
