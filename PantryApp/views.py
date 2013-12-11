from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from PantryApp.models import *
import random

def login(fn):
	def wrapper(self,request):
		comp = request.session.get('session_id')
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
        userName = request.POST["email"]
	userPass1 = request.POST["password1"]
	userPass2 = request.POST["password2"]

	person = User.objects.filter(email=userName)
	if any(person):
        	return render(request, 'PantryApp/register.html', {'email': userName})
	else:
		if (userPass1 != userPass2):
			return render(request, 'PantryApp/register.html', {'email': userName})
		else:
			userPass = make_password(userPass1,'pbkdf2_sha256')
			session_id = random.randint(1,9999999)
			person = User.objects.create(email=userName,password_hash=userPass,session_id=session_id)
			person.save()
			request.session['user_id'] = person.id
			return redirect('Pantry')

class Login(View):
    def get(self, request):
        return render(request, 'PantryApp/login.html')
    def post(self, request):
	userName = request.POST["email"]
	userPass = request.POST["password"]
	persons = User.objects.filter(email=userName)
	if any(persons):
		persons = User.objects.get(email=userName)
		userPassComp = make_password(userPass,'pbkdf2_sha256')
		if (persons.password_hash == userPassComp):
			persons.session_id = random.randint(1,9999999)
			persons.save()
			request.session['user_id'] = persons.id
       			return redirect('Pantry')
			#return HttpResponse(persons.id)
		else:
                	return render(request, 'PantryApp/login.html', {'email': userName})
	else:
		return render(request, 'PantryApp/login.html', {'email': userName})

class Pantry(View):
	@login
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
    def get(self, request, category):
        # Rendering example data
        return render(request, 'PantryApp/recipes.html',
                {"category": category,
                 "recipes": [
                    {'id': 1, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                    {'id': 2, 'name': 'Scrambled Eggs', 'link': 'www.food.com', 
                        'photo_exists': True },
                    {'id': 3, 'name': 'Grilled Cheese', 'link': 'www.food.com', 
                        'photo_exists': True },
                    {'id': 4, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                    {'id': 5, 'name': 'Chili', 'link': 'www.food.com', 
                        'photo_exists': False },
                ]})
