from django import forms
from RecipeBoxV1.models import Author, RecipeItem


class AuthorAddForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)


class RecipeItemAddForm(forms.ModelForm):
    class Meta:
        model = RecipeItem
        fields = [
            'author',
            'title',
            'body',
            'time_required',
            'instructions'
        ]
