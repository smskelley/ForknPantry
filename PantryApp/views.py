from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

# Register View
class Register(View):
    def get(self, request):
        return render(request, 'PantryApp/register.html')
    def post(self, request):
        # Rendering example data
        return render(request, 'PantryApp/register.html', { 'email': 'user@mail.com' })

class Login(View):
    def get(self, request):
        return render(request, 'PantryApp/login.html')
    def post(self, request):
        # Rendering example data
        return render(request, 'PantryApp/login.html', { 'email': 'user@mail.com' })

class Pantry(View):
    def get(self, request):
        # Rendering example data
        return render(request, 'PantryApp/pantry.html',
                {"ingredients": [
                    {'id': 1, 'ingredient': 'Milk', 'user_has': True },
                    {'id': 2, 'ingredient': 'Eggs', 'user_has': False },
                    {'id': 3, 'ingredient': 'Cheese', 'user_has': True },
                ]})
    def post(self, request):
        # Rendering example data
        return render(request, 'PantryApp/pantry.html',
                {"ingredients": [
                    {'id': 1, 'ingredient': 'Milk', 'user_has': False },
                    {'id': 2, 'ingredient': 'Eggs', 'user_has': True },
                    {'id': 3, 'ingredient': 'Cheese', 'user_has': False },
                ]})

class Recipes(View):
    def get(self, request):
        # Rendering example data
        return render(request, 'PantryApp/recipes.html',
                {"recipes": [
                    {'id': 1, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                    {'id': 2, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                    {'id': 3, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                ]})
