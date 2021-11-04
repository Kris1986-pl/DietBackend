# Generated by Django 3.2.7 on 2021-10-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_ingredient_meals_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='carbohydrates',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meal',
            name='fat',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meal',
            name='kcal',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meal',
            name='protein',
            field=models.SmallIntegerField(default=0),
        ),
    ]
