from django.urls import path

from . import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.website_homepage, name='website_homepage')

]