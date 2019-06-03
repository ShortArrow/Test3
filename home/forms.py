from django import forms
from .models import homeModel, Message

class homeForm(forms.ModelForm):
    class Meta:
        model = homeModel
        fields = ['name', 'mail', 'age', 'address', 'money']

class kensakuForm(forms.Form):  #本文のFindForm
    find = forms.CharField(label='address', required=False)

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['title', 'content', 'home']