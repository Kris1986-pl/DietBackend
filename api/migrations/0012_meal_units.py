# Generated by Django 3.2.7 on 2021-10-06 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_remove_meal_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='units',
            field=models.ManyToManyField(blank=True, through='api.Ingredient_Meals', to='api.Unit'),
        ),
    ]