from django.urls import path

from . import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.website_homepage, name='website_homepage'),
	path('map/', views.squirrel_map, name='squirrel_map'),
	path('sightings/', views.squirrel_list, name='squirrel_list')
]