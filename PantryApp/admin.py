from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from PantryApp.models import Ingredient, UserPantry, Category, Recipe

admin.site.register(UserPantry)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe)

#needed to make UserPantry play nicely with the built in User model
class UserPantryInline(admin.StackedInline):
	model = UserPantry
	can_delete = False
	verbose_name_plural = 'UserPantry'

#Define a new User admin
class UserAdmin(UserAdmin):
	inlines = (UserAdminInline,)

#Re-Register UserAdmin
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
