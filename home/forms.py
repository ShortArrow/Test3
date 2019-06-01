from django import forms
from.models import homeModel

class homeForm(forms.ModelForm):
    class Meta:
        model = homeModel
        fields = ['name', 'mail', 'age', 'address', 'money']

class kensakuForm(forms.Form):  #本文のFindForm
    find = forms.CharField(label='address', required=False)

