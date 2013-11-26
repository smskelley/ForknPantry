from django.db import models

# Ingredient Model
class Ingredient(models.Model):
        name = models.CharField(max_length=200)
        def __unicode__(self):
            return self.name

# Category Model
class Category(models.Model):
        name = models.CharField(max_length=200)
        def __unicode__(self):
            return self.name

# User Model
class User(models.Model):
	email = models.EmailField(max_length=254)
	password_hash = models.CharField(max_length=200)
	session_id = models.IntegerField()
	ingredients = models.ManyToManyField(Ingredient)
        def __unicode__(self):
            return self.email

# Recipe Model
class Recipe(models.Model):
	name = models.CharField(max_length=200)
	link = models.URLField()
	photo_exists = models.BooleanField()
	category = models.ForeignKey(Category)
	ingredients = models.ManyToManyField(Ingredient)
        def __unicode__(self):
            return self.name
