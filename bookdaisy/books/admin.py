from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Book, Profile

# Register your models here.
admin.site.register(Book)
admin.site.register(Profile)
admin.site.unregister(Group)
admin.site.unregister(User)

# add profile to user model
class ProfileInline(admin.StackedInline):
    model = Profile

# show profile with user
class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email']
    inlines = [ProfileInline]

admin.site.register(User, UserAdmin)