# Generated by Django 3.2.7 on 2021-10-12 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0048_auto_20211012_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='spice',
        ),
        migrations.AddField(
            model_name='meal',
            name='spice',
            field=models.ManyToManyField(to='api.Spice'),
        ),
    ]