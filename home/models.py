from django.db import models

# Create your models here.
class homeForm(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    money = models.IntegerField(default=0)

    def __str__(self):
            return '<Home Form:id=' + str(self.id) + ', ' + \
                self.name + '(' + str(self.age) + ')' + self.mail + ' ' + self.address + str(self.money)  + '>'



