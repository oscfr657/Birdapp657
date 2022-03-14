from django import forms


class SearchBirdForm(forms.Form):
    search_query = forms.CharField(label='Search', required=True)
