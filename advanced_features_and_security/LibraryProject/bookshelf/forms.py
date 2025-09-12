from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=200)
    email = forms.EmailField()

class BookSearchForm(forms.Form):
    query = forms.CharField(label="search", max_length=100)
