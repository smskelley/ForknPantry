from django.db import models
from django.contrib.auth.models import User

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

# UserPantry Model
class UserPantry(models.Model):
	user = models.OneToOneField(User)
	ingredients = models.ManyToManyField(Ingredient)
        def __unicode__(self):
            return self.user

# Recipe Model
class Recipe(models.Model):
	name = models.CharField(max_length=200)
	link = models.URLField()
	photo_exists = models.BooleanField()
	category = models.ForeignKey(Category)
	ingredients = models.ManyToManyField(Ingredient)
        def __unicode__(self):
            return self.name
