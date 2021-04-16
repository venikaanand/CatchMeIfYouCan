


# IEOR E4501: Tools for Analytics Project, Squirrel Tracker
A web-application for tracking squirrels in Central Park, New York City area

## Group Name: Project Group 30
### Group Member: Venika Anand, Chaitanya Varma Kanumuri 
### UNI: va2439, ck3025


## Introduction
This read me file explains our implementation for IEOR 4501 project. We are implementing a web application using Django, a web application tool leveraging Python to import, modify and implement data to build a Squirrel Tracking System with the intention to find squirrels in Central Park, New York City Area. 

## Functionality
The **Squirrel Tracking Web application** is based on Django development that helps track all squirrels in the Central Park, New York City area. 
In this web application, the dataset is imported. The users can view, update and add squirrel details as per current scenario. This web application gives an end-to-end facility to map and retrieve insights about squirrels which are mapped to unique squirrel IDs.

## Dataset
This dataset contains data from 3,018 different squirrel sightings, including location coordinates, age, primary and secondary fur color, elevation, activities, communications, and interactions between squirrels and with humans at the Central Park.

## Management Commands
**Import**: command that can import the data from the csv file, 2018 Central Park Squirrel Census. Specifically, the file path should be included after the management command in the command line.

python manage.py import_squirrel_data /path/to/file.csv

**Export**: command that can be used to export the data in a CSV format. Also, the file path should be added at the command line after the management command.

python manage.py export_squirrel_data /path/to/file.csv

## Dependencies
- [Django](https://www.djangoproject.com)
- [Django-Leaflet](https://django-leaflet.readthedocs.io/en/latest/) 

## Documentation Provided
The description for this project is in [**Squirrel Tracker**](https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit)

## Contributors

### Group Name: Project Group 30
Section: 1

**Contributors: Venika Anand, Chaitanya Varma Kanumuri**

**UNIs**: **[ va2439]** , **[ck3025]**

GitHub Link [**Link**](https://github.com/venikaanand/CatchMeIfYouCan) to our Squirrel Tracker application page for more information. 



