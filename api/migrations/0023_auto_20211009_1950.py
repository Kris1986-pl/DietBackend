# Generated by Django 3.2.7 on 2021-10-09 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_remove_ingredient_units'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient_meals',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='api.ingredient'),
        ),
        migrations.AlterField(
            model_name='ingredient_meals',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='api.unit'),
        ),
    ]
