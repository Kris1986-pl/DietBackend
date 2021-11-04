# Generated by Django 3.2.7 on 2021-10-09 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_meal_ingredients'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='units',
            field=models.ManyToManyField(through='api.Ingredient_Meals', to='api.Unit'),
        ),
    ]
