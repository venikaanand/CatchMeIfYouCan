from django.db import models

# Create your models here.
from django.utils import timezone
import datetime
from django.utils.translation import gettext as _

class SquirrelModel(models.Model):

    Latitude = models.FloatField(null=True)
    Longitude = models.FloatField(null=True)
    Unique_Squirrel_ID = models.CharField(max_length=14,primary_key=True)
    Hectare = models.CharField(max_length = 200,null=True,blank=True)
    Shift = models.CharField(choices = (('AM', 'AM'),('PM', 'PM')),max_length=14,default = 'AM',null=True)
    Date = models.DateField(null=True)
    Hectare_Squirrel_Number = models.CharField(max_length=200,null=True,blank=True)
    Age = models.CharField(choices = (('Adult', 'Adult'),('Juvenile', 'Juvenile'),('?', '?'),('', '')),max_length=14,default = '',null=True)
    Primary_Fur_Color = models.CharField(choices = (('Gray', 'Gray'),('Black', 'Black'),('Cinnammon', 'Cinnammon'),('', '')),max_length=14,default = '', null=True, blank=True)
    Highlight_Fur_Color = models.CharField(choices = (('Gray', 'Gray'),('Black', 'Black'),('Cinnammon', 'Cinnammon'),('White', 'White'), ( 'Black, Cinnammon', 'Black, Cinnammon'), ('Black, White', 'Black, White'),('Black, Cinnammon, White', 'Black, Cinnammon, White'), ('Cinammon, White', 'Cinammon, White'),('Gray, Black', 'Gray, Black'),('Black, White', 'Black, White'),('Gray, White', 'Gray, White'),('', '')),default = '',max_length = 200,null=True,blank=True)
    Combination_Fur = models.CharField(max_length = 200,null=True,default='',blank=True)
    Color_Notes = models.CharField(max_length=200,null=True,blank=True)
    Location = models.CharField( choices = (('Above Ground', 'Above Ground'),('Ground Plane', 'Ground Plane'),('', '')),default = '', max_length=200, null=True,blank=True)
    Above_Ground_Sighter_Measurement = models.CharField(max_length = 200,null=True,blank=True)
    Specific_Location = models.CharField(max_length=200,null=True,blank=True)
    Running = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Chasing = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Climbing = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Eating = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Foraging = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
	
    Other_Activities = models.CharField(max_length=200,null=True,blank=True)

    Kuks = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Quaas = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Moans = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Tail_Flags = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Tail_Twitches = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Approaches = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Indifferent = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
    Runs_From = models.CharField(choices=(('TRUE','true'),('FALSE','false')),default='FALSE',max_length=200,null=True)
	    
    Other_Interactions = models.CharField(max_length=200,null=True,blank=True)
	
    Lat_Long = models.CharField(max_length=200, null=True,blank=True)
	
	
	
	
	    
class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
	    return self.choice_text
		
from django.db import models
from django.utils.translation import gettext as _
