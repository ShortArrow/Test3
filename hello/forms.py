from django import forms

class HelloForm(forms.Form):
    name = forms.CharField(label='name')
    mail = forms.CharField(label='mail')
    age = forms.IntegerField(label='age')
    address = forms.CharField(label='address')
    money = forms.IntegerField(label='money')
    monkey = forms.CharField(label='monkey')
