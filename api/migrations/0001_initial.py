# Generated by Django 3.2.7 on 2021-10-05 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('macro', models.SmallIntegerField(default=0)),
                ('kcal', models.SmallIntegerField(default=0)),
                ('protein', models.SmallIntegerField(default=0)),
                ('carbohydrates', models.SmallIntegerField(default=0)),
                ('fat', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient_Meals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.ingredient')),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.meal')),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='meals',
            field=models.ManyToManyField(through='api.Ingredient_Meals', to='api.Meal'),
        ),
        migrations.AddConstraint(
            model_name='ingredient_meals',
            constraint=models.UniqueConstraint(fields=('meal', 'ingredient'), name='once_per_product_sale'),
        ),
    ]
