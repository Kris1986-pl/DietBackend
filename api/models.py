from django.db import models
from django.contrib.auth.models import User


class Spice(models.Model):
    name = models.CharField(max_length=32, default='', null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Meal(models.Model):
    day = models.SmallIntegerField(default=1)
    counter = models.SmallIntegerField(default=1)
    title = models.CharField(max_length=256, )
    description = models.TextField(max_length=1024)
    kcal = models.SmallIntegerField(default=0)
    protein = models.SmallIntegerField(default=0)
    carbohydrates = models.SmallIntegerField(default=0)
    fat = models.SmallIntegerField(default=0)
    user = models.ManyToManyField(User)
    ingredients = models.ManyToManyField('Ingredient', through='IngredientMeals')
    spice = models.ManyToManyField(Spice, blank=True)

    class Meta:
        ordering = ['day', 'counter']

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=256, default='')
    kcal = models.SmallIntegerField(default=0)
    protein = models.SmallIntegerField(default=0)
    carbohydrates = models.SmallIntegerField(default=0)
    fat = models.SmallIntegerField(default=0)
    units = models.ManyToManyField('Unit', through='IngredientMeals', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Unit(models.Model):
    name = models.CharField(max_length=32, default='')

    def __str__(self):
        return self.name


class IngredientMeals(models.Model):
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE, related_name='igredientmeals')
    ingredient = models.ForeignKey('Ingredient', on_delete=models.CASCADE, related_name='ingredients')
    quantity = models.DecimalField(default=1, max_digits=999, decimal_places=1)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name='units')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=('meal', 'ingredient'), name='once_per_meal_ingredient')
        ]

    def __str__(self):
        return self.name()

    def name(self):
        return "{} --> {}".format(self.meal, self.ingredient)
