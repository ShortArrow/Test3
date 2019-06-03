from django.db import models

# Create your models here.
class homeModel(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    money = models.IntegerField(default=0)

    def __str__(self):
            return '<Home Form:id=' + str(self.id) + ', ' + \
                self.name + '(' + str(self.age) + ')' + self.mail + ' ' + self.address + str(self.money)  + '>'

class Message(models.Model):
    home = models.ForeignKey(homeModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '<Message:id=' + str(self.id) + ', ' + \
            self.title + '(' + str(self.pub_date) + ')>'
    
    class Meta:
        ordering = ('pub_date',)
        


