from django.db import models

# User Model
class User(models.Model):
	email = models.EmailField(max_length=254)
	password_hash = models.CharField(max_length=200)
	session_id = models.IntegerField()
	ingredients = models.ManyToManyField(Ingredient)
	class Meta:
		app_label = 'PantryApp'

# Ingredient Model
class Ingredient(models.Model):
	name = model.CharField(max_length=200)
	class Meta:
		app_label = 'PantryApp'

# Recipe Model
class Recipe(models.Model):
	name = models.CharField(max_length=200)
	link = models.URLField()
	photo_exists = models.BooleanField()
	category = models.ForeignKey(Category)
	ingredients = models.ManyToManyField(Ingredient)

# Category Model
class Category(models.Model):
	name = models.CharField(max_length=200)
