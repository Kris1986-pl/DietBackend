# Generated by Django 3.2.7 on 2021-10-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_unit_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='macro',
        ),
        migrations.AlterField(
            model_name='ingredient_meals',
            name='quantity',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=999),
        ),
    ]