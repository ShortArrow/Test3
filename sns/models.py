from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Message(models.Model):   #メッセージ投稿のためのデータベース設計、レコードのためのテーブルをつくる
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_owner')
    # ForeignKeyの引数に、モデルを指定すると、そのモデルと関連付けをすることができる  リレーションシップがとれる
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    # ForeignKeyがあるから、従テーブルであるとわかる 絶対にないといけないテーブルが主テーブル groupがないと、messageは存在しない
    content = models.TextField(max_length=1000)
    share_id = models.IntegerField(default=-1)
    good_count = models.IntegerField(default=0)
    share_count = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):   #クラスを文字列として表示するため
        return str(self.content) + '(' + str(self.owner) + ')'
    #クラスのインスタンスの表示の設定ができる

    def get_share(self):
        return Message.objects.get(id=self.share_id)
        # object.get() データベースにあるレコードを取り出す　　引数のIDに番号を指定するとその番号のインスタンスが取得される

    class Meta:
        ordering = ('-pub_date',)

class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_owner')  #主テーブルとリレーションシップを取得
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_owner') #主テーブルとリレーションシップ
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + '(group:"' + str(self.group) + '")'

class Good(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='good_owner')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return 'good for "' + str(self.message) + '" (by ' + str(self.owner) + ')'
        





