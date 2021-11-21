from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
from userprofile.models import UserProfile


class userProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name_plural = "profile"

class UserAdmin(UserAdmin):
    inlines = (userProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
