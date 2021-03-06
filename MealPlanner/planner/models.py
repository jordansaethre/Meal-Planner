from django.db import models

class Meals(models.Model):
	MEAL_TYPES = [('B', "Breakfast"), ('L', "Lunch"), ('D', "Dinner"), ('S', "Snack")]
	meal_title = models.CharField(max_length = 100)
	meal_type = models.CharField(max_length = 10, choices = MEAL_TYPES, blank=True)
	def __str__(self):
		return self.meal_title