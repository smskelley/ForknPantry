from django.contrib import admin
from PantryApp.models import Ingredient, User, Category, Recipe

admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe)
