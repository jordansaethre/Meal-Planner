from csv import DictReader
from datetime import datetime

from django.core.management import BaseCommand

from planner.models import Meals
from pytz import UTC


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the meals data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    # Show this when the user types help
    help = "Loads data from meals.csv into our Meals model"

    def handle(self, *args, **options):
        if  Meals.objects.exists():
            print('Meals data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return
        print("Creating meals data")
        print("Loading meals data for meals available for meal planner")
        for row in DictReader(open('./meals.csv')):
            meal = Meals()
            meal.meal_title = row['meal_title']
            meal.meal_type = row['meal_type']
            meal.save()
