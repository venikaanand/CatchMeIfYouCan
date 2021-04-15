from django.forms import ModelForm
from .models import SquirrelModel


class SquirrelAllForm(ModelForm):
	class Meta:
		model = SquirrelModel
		fields = '__all__'
		#fields = ['Latitude', 'Longitude', 'Unique_Squirrel_ID', 'Shift','Date','Age']
