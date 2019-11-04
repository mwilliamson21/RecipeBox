from django.shortcuts import (
    render, HttpResponseRedirect, reverse
)
from RecipeBoxV1.forms import RecipeItemAddForm, AuthorAddForm
from RecipeBoxV1.models import RecipeItem, Author


def index(request):
    html = 'index.html'

    data = RecipeItem.objects.all()

    return render(request, html, {'data': data})


def read_recipe(request, id):
    recipe_html = "recipes.html"

    recipe_data = RecipeItem.objects.filter(id=id)
    return render(request, recipe_html, {'data': recipe_data})


def author_view(request, id):
    author_html = 'authors.html'
    author = Author.objects.filter(id=id)
    recipes = RecipeItem.objects.filter(author=id)

    return render(
        request, author_html, {'data': author, 'recipes': recipes}
    )


def authoraddview(request):
    html = "generic_form.html"

    if request.method == "post":
        form = AuthorAddForm(request.Post)

        if form.is_valid():
            data = form.cleaned_data
            Author.objects.create(name=data['name'])
            return HttpResponseRedirect(reverse('homepage'))

    form = AuthorAddForm()

    return render(request, html, {'form': form})


def recipeaddview(request):
    html = 'add_recipe.html'

    if request.method == 'POST':
        form = RecipeItemAddForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse('homepage'))

    form = RecipeItemAddForm()

    return render(request, html, {'form': form})
