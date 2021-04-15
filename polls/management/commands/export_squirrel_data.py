from polls.models import SquirrelModel
import csv

from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs['path'], 'w', newline='') as csvfile:
            attributes = ['Latitude', 
            			'Longitude', 
            			'Unique_Squirrel_ID', 
						'Hectare',
            			'Shift', 
            			'Date', 
						'Hectare_Squirrel_Number',
            			'Age', 
            			'Primary_Fur_Color',
						'Highlight_Fur_Color',
					    'Combination_Fur',
						'Color_Notes',
            			'Location',
						'Above_Ground_Sighter_Measurement',
                        'Specific_Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other_Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
                        'Tail_Flags',
                        'Tail_Twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs_From',
						'Other_Interactions',
						'Lat_Long']
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            writer.writerow(attributes)
            for row in SquirrelModel.objects.all():
                writer.writerow([getattr(row, attribute) for attribute in attributes])
        csvfile.close
