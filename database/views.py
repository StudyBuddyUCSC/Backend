from django.shortcuts import render
from database.models import Location

locations = [
    {'location_name': 'SNE Libary', 'location_type': 'Libary', 'campus_location': 'Science Hill', 'allhouraccess': False, 'genderneutralbathroom': True},
    {'location_name': 'McHenry', 'location_type': 'Libary', 'campus_location': 'Central Core', 'allhouraccess': False, 'genderneutralbathroom': True},
    {'location_name': 'Baskin Engineering 105', 'location_type': 'Classroom', 'campus_location': 'Baskin', 'allhouraccess': True, 'genderneutralbathroom': False},
    {'location_name': 'Page Smith Libary', 'location_type': 'Libary', 'campus_location': 'Cowell', 'allhouraccess': False, 'genderneutralbathroom': False},
    {'location_name': 'Stevenson Libary', 'location_type': 'Libary', 'campus_location': 'Stevenson', 'allhouraccess': True, 'genderneutralbathroom': False},
    {'location_name': 'Terry Frietas Cafe', 'location_type': 'Cafe', 'campus_location': 'Cowell', 'allhouraccess': False, 'genderneutralbathroom': True}, 
    # ...
]

# Create your views here.
