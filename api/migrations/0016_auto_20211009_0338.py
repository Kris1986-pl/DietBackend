# Generated by Django 3.2.7 on 2021-10-09 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_auto_20211008_2053'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['day', 'counter']},
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='meals',
        ),
        migrations.AlterField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(through='api.Ingredient_Meals', to='api.Ingredient'),
        ),
    ]