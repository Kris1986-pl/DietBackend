# Generated by Django 3.2.7 on 2021-10-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0032_auto_20211010_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='meal',
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(through='api.Ingredient_Meals', to='api.Ingredient'),
        ),
    ]
