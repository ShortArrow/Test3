from django.contrib import admin
from .models import Message,Friend,Group,Good
# Register your models here.

admin.site.register(Message)   #管理ツールに登録する　　管理ツールを使うとテーブルの編集が可能になる
admin.site.register(Friend)
admin.site.register(Group)
admin.site.register(Good)

