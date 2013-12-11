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
			user_ingredients = User.objects.get(id=request.user.id).userpantry.ingredients.count()
			if user_ingredients is None:
				return redirect('Pantry')
			else:
				return redirect('Recipes',category='lunch')
		else:
			return redirect('Login')

# Register View
class Register(View):
	def get(self, request):
		return render(request, 'PantryApp/register.html')
	def post(self, request):
		userName = request.POST["username"]
		userPass1 = request.POST["password1"]
		userPass2 = request.POST["password2"]
		person = User.objects.filter(username=userName)
		if person is None:
			return render(request, 'PantryApp/register.html', {'username': userName})
		else:
			if (userPass1 != userPass2):
				return render(request, 'PantryApp/register.html', {'username': userName})
			else:
				person = User.objects.create_user(userName,userName,userPass1)
				person.is_active = True
				person.save()
				userPantry = UserPantry(user=person)
				userPantry.save()
				user = authenticate(username=userName,password=userPass1)
				login(request,user)
				return redirect('Pantry')

class LoginUser(View):
    def get(self, request):
        return render(request, 'PantryApp/login.html')
    def post(self, request):
	userName = request.POST["username"]
	userPass = request.POST["password"]
	user = authenticate(username=userName,password=userPass)
    	if user is not None:
        	if user.is_active:
			login(request,user)
			return redirect('Pantry')
		else:
			return render(request, 'PantryApp/login.html', {'username': userName})
	else:
		return render(request, 'PantryApp/login.html', {'username': userName})

class Pantry(View):
    @method_decorator(login_required)
    def get(self, request):

	ingredients = Ingredient.objects.all()
	user_ingredients = User.objects.get(id=request.user.id).userpantry.ingredients.all()
	row = {}
	final_list = []
	for ingredient in ingredients:
		row['id'] = ingredient.id
		row['ingredient'] = ingredient.name
		row['user_has'] =  ingredient in user_ingredients
		final_list.append(row.copy())
		print (row['ingredient'])
	print len(final_list)	
        # Rendering example data
        return render(request, 'PantryApp/pantry.html', {"ingredients" : final_list})
    
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
