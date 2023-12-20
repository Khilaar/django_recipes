from django.urls import path

from recipe.views import ListCreateRecipeView, RetrieveUpdateDeleteRecipeView

urlpatterns = [
    path("", ListCreateRecipeView.as_view()),
    path("<int:id>/", RetrieveUpdateDeleteRecipeView.as_view())
]