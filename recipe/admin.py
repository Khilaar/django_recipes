from django.contrib import admin

from recipe.models import recipe


# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("title", "difficulty", "ingredients")
    search_fields = ("title", "difficulty", "ingredients")
    list_filter = ("title", "difficulty")
    ordering = ("difficulty",)


admin.site.register(recipe, RecipeAdmin)
