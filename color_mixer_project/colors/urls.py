from django.urls import path
from . import views

urlpatterns = [
    path("", views.color_list, name="color_list"),
    path('recipes/', views.recipe_list, name='recipe_list'),
]