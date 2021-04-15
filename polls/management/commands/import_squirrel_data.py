from django.core.management.base import BaseCommand
from polls.models import SquirrelModel
import requests, csv, re, sys
from dateutil import parser
from datetime import date

class Command(BaseCommand):
   
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        
        pattern = re.compile(r'(\d{2})(\d{2})(\d{4})') # regex pattern for dates
        
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            next(reader)
            unique_id = list()
            for row in reader: # loop through each row in df
                if row[2] in unique_id: #check if a squirrel id is already taken care of
                    continue
                else:
                    month, day, year = pattern.match(row[5]).groups() #pick year month and date from regex
                    squirrel = SquirrelModel.objects.get_or_create(
                        Latitude = float(row[0]),
                        Longitude = float(row[1]),
                        Unique_Squirrel_ID = row[2],
                        Hectare = row[3],
						Shift = row[4],
                        Date = date(int(year), int(month), int(day)), #taking care of date pattern
						Hectare_Squirrel_Number = row[6],
                        Age = row[7],
                        Primary_Fur_Color = row[8],
						Highlight_Fur_Color = row[9],
						Combination_Fur = row[10],
						Color_Notes = row[11],
                        Location = row[12],
						Above_Ground_Sighter_Measurement = row[13],
						Specific_Location = row[14],
                        Running = row[15],
                        Chasing = row[16] ,
                        Climbing =  row[17] ,
                        Eating = row[18] ,
                        Foraging = row[19] ,
                        Other_Activities =  row[20] ,
                        Kuks = row[21] ,
                        Quaas = row[22] ,
                        Moans = row[23] ,
                        Tail_Flags = row[24] ,
                        Tail_Twitches = row[25] ,
                        Approaches = row[26] ,
                        Indifferent = row[27] ,
                        Runs_From = row[28],
						Other_Interactions = row[29],
						Lat_Long = row[30]
                    )
                    unique_id.append(row[2]) #append squirrel id to list so that we dont consider same one again