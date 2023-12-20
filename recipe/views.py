import json

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views import View

from recipe.models import recipe


# Create your views here.


class ListCreateRecipeView(View):
    def get(self, request, *args, **kwargs):
        # 1. get all recipes from db
        recipes = recipe.objects.all().values()
        # 2. return all the recipes in json format
        return JsonResponse(list(recipes), safe=False)

    def post(self, request, *args, **kwargs):
        # 1. get data from user, transform to python
        if request.body:
            data = json.loads(request.body)
            # 2. use ORM to create the recipe
            new_recipe = recipe.objects.create(**data)
            # 3. create a dictionary from the response
            response_data = recipe.objects.values("id", "title", "ingredients", "description", "favorite",
                                                  "difficulty").get(id=new_recipe.id)
            # 4. return json data (optional)
            return JsonResponse(response_data, status=201)
        return JsonResponse({"message": "Request boy is empty"}, status=400)


class RetrieveUpdateDeleteRecipeView(View):
    def get(self, request, *args, **kwargs):
        recipe_id = kwargs.get("id")
        try:
            getted_recipe = recipe.objects.get(id=recipe_id)
            response_data = {
                "id": getted_recipe.id,
                "title": getted_recipe.title,
                "ingredients": getted_recipe.ingredients,
                "description": getted_recipe.description,
                "favorite": getted_recipe.favorite,
                "difficulty": getted_recipe.difficulty,
            }
            return JsonResponse(response_data)
        except recipe.DoesNotExist:
            return JsonResponse({"message": f"Recipe with id {recipe_id} does not exist"})

    def patch(self, request, *args, **kwargs):
        if not request.body:
            return JsonResponse({"message": "The request body is empty"}, status=400)
        recipe_id = kwargs.get("id")
        try:
            getted_recipe = recipe.objects.get(id=recipe_id)

            data = json.loads(request.body)
            for key, value in data.items():
                setattr(getted_recipe, key, value)
            getted_recipe.save()

            response_data = {
                "id": getted_recipe.id,
                "title": getted_recipe.title,
                "ingredients": getted_recipe.ingredients,
                "description": getted_recipe.description,
                "favorite": getted_recipe.favorite,
                "difficulty": getted_recipe.difficulty,
            }
            return JsonResponse(response_data, status=200)
        except recipe.DoesNotExist:
            return JsonResponse({"message": f"Recipe with id {recipe_id} does not exist"})

        except recipe.DoesNotExist:
            return JsonResponse({"message": f"Recipe with id {recipe_id} does not exist"})
        pass

    def delete(self, request, *args, **kwargs):
        recipe_id = kwargs.get("id")
        try:
            getted_recipe = recipe.objects.get(id=recipe_id)
            response_data = {
                "id": getted_recipe.id,
                "title": getted_recipe.title,
                "ingredients": getted_recipe.ingredients,
                "description": getted_recipe.description,
                "favorite": getted_recipe.favorite,
                "difficulty": getted_recipe.difficulty,
            }
            getted_recipe.delete()
            return HttpResponse(status=204)
        except recipe.DoesNotExist:
            return JsonResponse({"message": f"Recipe with id {recipe_id} does not exist"})
        pass
