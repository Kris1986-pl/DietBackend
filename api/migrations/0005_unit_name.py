# Generated by Django 3.2.7 on 2021-10-05 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211005_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='name',
            field=models.CharField(default='', max_length=32),
        ),
    ]