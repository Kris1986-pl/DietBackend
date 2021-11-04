from django.contrib import admin
from .models import Meal, Unit, Spice, Ingredient, IngredientMeals

admin.site.register(Meal)
admin.site.register(Unit)
admin.site.register(Spice)
admin.site.register(Ingredient)
admin.site.register(IngredientMeals)
