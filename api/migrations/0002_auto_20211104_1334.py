# Generated by Django 3.2.7 on 2021-11-04 13:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientMeals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=1, default=1, max_digits=999)),
            ],
        ),
        migrations.CreateModel(
            name='Spice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32)),
            ],
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'ordering': ['name']},
        ),
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ['day', 'counter']},
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='macro',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='meals',
        ),
        migrations.AddField(
            model_name='meal',
            name='carbohydrates',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='meal',
            name='counter',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='meal',
            name='day',
            field=models.SmallIntegerField(default=1),
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
        migrations.AddField(
            model_name='meal',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Ingredient_Meals',
        ),
        migrations.AddField(
            model_name='ingredientmeals',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='api.ingredient'),
        ),
        migrations.AddField(
            model_name='ingredientmeals',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='igredientmeals', to='api.meal'),
        ),
        migrations.AddField(
            model_name='ingredientmeals',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='units', to='api.unit'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='units',
            field=models.ManyToManyField(blank=True, through='api.IngredientMeals', to='api.Unit'),
        ),
        migrations.AddField(
            model_name='meal',
            name='ingredients',
            field=models.ManyToManyField(through='api.IngredientMeals', to='api.Ingredient'),
        ),
        migrations.AddField(
            model_name='meal',
            name='spice',
            field=models.ManyToManyField(blank=True, to='api.Spice'),
        ),
        migrations.AddConstraint(
            model_name='ingredientmeals',
            constraint=models.UniqueConstraint(fields=('meal', 'ingredient'), name='once_per_meal_ingredient'),
        ),
    ]
