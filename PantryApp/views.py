from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore
from django.contrib.auth.hashers import make_password
from PantryApp.models import *
import random

def login(fn):
	def wrapper(self,request):
		comp = 1
		if (comp):
			return fn(self,request)
		else:
			return redirect('Login')
	return wrapper

# Register View
class Register(View):
    def get(self, request):
        return render(request, 'PantryApp/register.html')
    def post(self, request):
        userName = request.POST["username"]
	userPass1 = request.POST["password1"]
	userPass2 = request.POST["password2"]
	person = User.objects.filter(username=userName)
	if any(person):
        	return render(request, 'PantryApp/register.html', {'username': userName})
	else:
		if (userPass1 != userPass2):
			return render(request, 'PantryApp/register.html', {'username': userName})
		else:
			userPantry = UserPantry
			session_id = random.randint(1,9999999)
			person = User.objects.create_user(userName,userName,userPass1)
			person.is_active = True
			person.save()
			userPantry.user = person
			userPantry.save()
			request.session['user_id'] = person.id
			return redirect('Pantry')

class LoginUser(View):
    def get(self, request):
        return render(request, 'PantryApp/login.html')
    def post(self, request):
	userName = request.POST["username"]
	userPass = request.POST["password"]
	user = User.objects.get(username__exact=userName)
    	if user is not None:
        	if user.is_active:
			if (user.check_password(userPass)):
				#s = Session.objects.get(pk=request.session)
				#return HttpResponse(s.session_data)
				login(request,user)
				return redirect('Pantry')
			else:
				return render(request, 'PantryApp/login.html', {'username': userName})
		else:
			return render(request, 'PantryApp/login.html', {'username': userName})
	else:
		return render(request, 'PantryApp/login.html', {'username': userName})

class Pantry(View):
    def get(self, request):

	ingredients = Ingredient.objects.all()
	user_ingredients = User.objects.get(email='seanlaue@gmail.com').ingredients.all()
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
