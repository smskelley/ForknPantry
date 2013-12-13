from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from PantryApp.models import *


# Home View
class Home(View):
    def get(self,request):
        if request.user.is_authenticated():
            number_of_ingredients = User.objects.get(id=request.user.id). \
                                    userpantry.ingredients.count()
            if number_of_ingredients == 0:
                return redirect('Pantry')
            else:
                return redirect('Recipes',category='lunch')
        return redirect('Login')


# Register View
class Register(View):
    def get(self, request):
        return render(request, 'PantryApp/register.html')
    def post(self, request):
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        if (User.objects.filter(username=username).exists() or
                password1 != password2):
            return render(request, 'PantryApp/register.html', 
                          {'username': username})

        person = User.objects.create_user(username=username,
                                          password=password1)
        person.save()
        pantry = UserPantry(user=person)
        pantry.save()
        user = authenticate(username=username,password=password1)
        login(request,user)
        return redirect('Pantry')


class LoginUser(View):
    def get(self, request):
        return render(request, 'PantryApp/login.html')
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username,password=password)
        if user is not None and user.is_active:
            login(request,user)
            return redirect('Pantry')

        return render(request, 'PantryApp/login.html', {'username': username})


class Pantry(View):
    @method_decorator(login_required)
    def get(self, request):
        ingredients = Ingredient.objects.all()
        user_ingredients = User.objects.get(id=request.user.id). \
                           userpantry.ingredients.all()
        row = {}
        final_list = []
        for ingredient in ingredients:
            row['id'] = ingredient.id
            row['ingredient'] = ingredient.name
            row['user_has'] = ingredient in user_ingredients
            final_list.append(row.copy())
        return render(request, 'PantryApp/pantry.html',
                      {"ingredients" : final_list})
    
    def post(self, request):
        # Rendering example data
        return render(request, 'PantryApp/pantry.html',
                {"ingredients": [
                    {'id': 1, 'ingredient': 'Milk', 'user_has': False },
                    {'id': 2, 'ingredient': 'Eggs', 'user_has': True },
                    {'id': 3, 'ingredient': 'Cheese', 'user_has': False },
                ]})


class Recipes(View):
    def get(self, request, category):
        # Rendering example data
        return render(request, 'PantryApp/recipes.html',
                {"category": category,
                 "recipes": [
                    {'id': 1, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                    {'id': 2, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                    {'id': 3, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                ]})
