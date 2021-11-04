# Generated by Django 3.2.7 on 2021-10-08 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20211007_1232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.DecimalField(decimal_places=1, default=1, max_digits=999)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.ManyToManyField(blank=True, through='api.Ingredient_Meals', to='api.Quantity'),
        ),
        migrations.AlterField(
            model_name='ingredient_meals',
            name='quantity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.quantity'),
        ),
    ]