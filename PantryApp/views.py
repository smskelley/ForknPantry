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
    
    @method_decorator(login_required)
    def post(self, request):
        # Update the user's ingredients based on POST data.
        # First check if current ingredients should remain ingredients and
        # then check if there are any new ingredients to add. This is likely
        # inefficient. If speed becomes an issue, fix this.
        pantry = User.objects.get(id=request.user.id).userpantry
        for ingredient in pantry.ingredients.all():
            if str(ingredient.id) not in request.POST:
                pantry.ingredients.remove(ingredient)
        for k in request.POST.keys():
            if k.isdigit():
                pantry.ingredients.add(
                        Ingredient.objects.get(id=int(k)))

        # For now, simply use get to display the information.
        # Surely inefficient, but functions fine in small scale.
        return self.get(request)

class Recipes(View):
    @method_decorator(login_required)
    def get(self, request, category):
        # This is an inefficient solution. It could certainly be enhanced.
        user_ingredients = set(User.objects.get(id=request.user.id). \
                           userpantry.ingredients.all())
        recipes = []
        # Go through all recipes in this category, compare recipe ingredients
        # against user ingredients. If the intersection between these sets is
        # the same length as the number of ingredients in the recipe, then
        # the user has all ingredients.
        for recipe in Recipe.objects.filter(
                category=Category.objects.get(name=category)):
            if (len(set(recipe.ingredients.all()) & user_ingredients) ==
                    recipe.ingredients.count()):
                row = { 'id': recipe.id,
                        'name': recipe.name,
                        'link': recipe.link,
                        'photo_exists': recipe.photo_exists, }
                recipes.append(row.copy())

        return render(request, 'PantryApp/recipes.html',
                {"category": category,
                 "recipes": recipes })
