from django.http import HttpResponse
from django.views.generic.base import View

# Register View
class Register(View):
	
	def get(self, request):
		return ("Hello, World!")

