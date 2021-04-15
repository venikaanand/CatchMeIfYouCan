<<<<<<< HEAD
from django.urls import path

from . import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.website_homepage, name='website_homepage')

=======
from django.urls import path

from . import views

apps_name = 'sightings'
urlpatterns = [
    path('', views.website_homepage, name='website_homepage')
>>>>>>> d4b35acf0fc875078ef573a2c8764e055609208a
]