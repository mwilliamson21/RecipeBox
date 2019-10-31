from django.shortcuts import render

from RecipeBoxV1.models import RecipeItem, Author


def index(request):
    html = "index.html"

    data = RecipeItem.objects.all()

    return render(request, html, {'data': data})


def read_recipe(request, id):
    recipe_html = "recipes.html"

    recipe_data = RecipeItem.objects.filter(id=id)
    return render(request, recipe_html, {'data': recipe_data})


def authors_info(request, id):
    author_html = "author.html"

    author_data = Author.objects.filter(id=id)

    recipe_data = RecipeItem.objects.filter(author=id)
    return render(request, author_html, {
        'data': author_data, 'recipes': recipe_data})
