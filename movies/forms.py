from django import forms

class Create(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    rating = forms.IntegerField(label="Rating")
    notes= forms.TextField()
    url = forms.CharField(max_length=255)

