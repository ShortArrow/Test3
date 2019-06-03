from django import forms
from .models import Message, Group, Friend, Good
from django.contrib.auth.models import User

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100)   #検索をするためのフォームを作成

class GroupCheckForm(forms.Form):
    def __init__(self, user, *args, **kwargs): # __init__（初期化メソッド）を定義すると、クラスをインスタント化する際に、引数を渡すことができる
        super(GroupCheckForm, self).__init__(*args, **kwargs).first()  #super()は、親クラス(基底クラス)を表すためのメソッド
        #基底クラスから、継承している
        public = User.objects.filter(username='public').first()
        #usernameからpublicを検索し、一番最初を取り出す
        

