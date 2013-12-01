from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View

# Register View
class Register(View):
	def get(self, request):
		return render(request, 'PantryApp/register.html')

class Login(View):
	def get(self, request):
		return render(request, 'PantryApp/login.html')

class Pantry(View):
	def get(self, request):
		return render(request, 'PantryApp/pantry.html')

class Recipes(View):
	def get(self, request):
		return render(request, 'PantryApp/recipes.html')
