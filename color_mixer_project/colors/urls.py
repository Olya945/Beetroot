from django.urls import path
from . import views

urlpatterns = [
    path("", views.color_list, name="color_list"),
    path("recipes/", views.recipe_list, name="recipe_list"),
    path("mix/", views.what_can_i_mix, name="what_can_i_mix"),
]