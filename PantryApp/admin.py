from django.contrib import admin
from PantryApp.models import Ingredient, UserPantry, Category, Recipe

admin.site.register(UserPantry)
admin.site.register(Ingredient)
admin.site.register(Category)
admin.site.register(Recipe)
