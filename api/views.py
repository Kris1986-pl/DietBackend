from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer
from .models import Meal, Ingredient, IngredientMeals
from .serializers import MealSerializer, IngredientMealsSerializer #,IngredientSerializer


class IngredientMealsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    # Find all the groups with a member whose name starts with 'Paul'
    Group.objects.filter(members__name__startswith='Paul')
    """
    queryset = IngredientMeals.objects.all()
    serializer_class = IngredientMealsSerializer
    # queryset = Ingredient_Meals.objects.filter(meal__id__startswith='1')
    # serializer_class = IngredientMealsSerializer


# class IngredientViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = Ingredient.objects.all()
#     serializer_class = IngredientSerializer


class MealViewSet(viewsets.ModelViewSet):

    queryset = Meal.objects.all()
    serializer_class = MealSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]