from django.forms import ModelForm
from .models import SquirrelModel


class SquirrelAllForm(ModelForm):
	class Meta:
		model = SquirrelModel
		fields = '__all__'
		#fields = ['Latitude', 'Longitude', 'Unique_Squirrel_ID', 'Shift','Date','Age']

class SquirrelAddForm(ModelForm):
	class Meta:
		model = SquirrelModel
		#fields = '__all__'
		fields = ['Latitude', 'Longitude', 'Unique_Squirrel_ID', 'Shift','Date','Age','Primary_Fur_Color','Location','Specific_Location','Running','Chasing', 'Climbing', 'Eating','Foraging','Other_Activities','Kuks','Quaas','Moans',  'Tail_Flags', 'Tail_Twitches', 'Approaches', 'Indifferent',  'Runs_From']
