from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Meal, Ingredient, Unit, IngredientMeals
from django.db import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']


class SpiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ['id', 'name']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = IngredientMeals
        fields = ['id', 'name']


class IngredientMealsSerializer(serializers.ModelSerializer):
    ingredient = IngredientSerializer()
    unit = UnitSerializer()

    class Meta:
        model = IngredientMeals
        fields = ['quantity', 'ingredient', 'unit']


class MealSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=True)
    spice = SpiceSerializer(many=True)
    igredientmeals = IngredientMealsSerializer(many=True, read_only=True)

    class Meta:
        model = Meal
        fields = ['id', 'day', 'counter', 'title', 'description', 'kcal', 'protein', 'carbohydrates', 'fat', 'user',
                  'spice', 'igredientmeals']
