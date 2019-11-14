from django import forms
from RecipeBoxV1.models import RecipeItem


class AuthorAddForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)
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


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

# class SignUpForm(forms.Form):
#     username = forms.CharField(max_length=50)
#     password = forms.CharField(widget=forms.PasswordInput)
