from django.conf.urls import patterns, include, url
from PantryApp.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^login/$', Login.as_view(), name='Login'),
    url(r'^register/$', Register.as_view(), name='Register'),
    url(r'^pantry/$', Pantry.as_view(), name='Pantry'),
    # recipes url will need to be updated to accept a type.
    # e.g. recipes/breakfast, recipes/lunch, etc
    url(r'^recipes/(?P<category>\w+)$', Recipes.as_view(), name='Recipes'),

    url(r'^admin/', include(admin.site.urls)),
)
