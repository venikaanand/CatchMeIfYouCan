from django.urls import path

from . import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.website_homepage, name='website_homepage'),
	path('map/', views.squirrel_map, name='squirrel_map'),
	path('sightings/', views.squirrel_list, name='squirrel_list'),
    path('sightings/stats/', views.squirrel_stats, name = 'squirrel_stats'),
    path('sightings/add/', views.squirrel_add, name = 'squirrel_add'),
    path('sightings/<str:squirrel_id>/', views.squirrel_details, name='squirrel_details'),
	path('sightings/<str:squirrel_id>/update', views.squirrel_modify, name='squirrel_modify'),
]