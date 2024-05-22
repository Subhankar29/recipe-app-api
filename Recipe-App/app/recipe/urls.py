"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)
# It is used to automatically assing different end points from the recipes route
from rest_framework.routers import DefaultRouter

from recipe import views


router = DefaultRouter()
router.register('recipes', views.RecipeViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls)),
]
