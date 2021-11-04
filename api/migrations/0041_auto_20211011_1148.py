# Generated by Django 3.2.7 on 2021-10-11 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0040_auto_20211011_1131'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meal',
            old_name='ingredient',
            new_name='ingredients',
        ),
        migrations.AlterField(
            model_name='ingredient_meals',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='api.ingredient'),
        ),
    ]