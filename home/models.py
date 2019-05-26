from django.db import models
from django.contrib.auth.models import User


class homeModel(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    money = models.IntegerField(default=0)

    def __str__(self):
        return '<Home Form:id=' + str(self.id) + ', ' + \
            self.name + '(' + str(self.age) + ')' + self.mail + \
            ' ' + self.address + str(self.money) + '>'


class ownerModel(models.Model):
    id_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class roomModel(models.Model):
    id_owner = models.ForeignKey(
        ownerModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class openPatternModel(models.Model):
    id_room = models.ForeignKey(
        roomModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class roomGroupModel(models.Model):
    id_room = models.ForeignKey(
        roomModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class timeTableModel(models.Model):
    id_openpattern = models.ForeignKey(
        openPatternModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    startTime = models.TimeField(auto_now_add=True)
    endTime = models.TimeField(auto_now_add=True)
    price = models.IntegerField(default=0)


class illegalDayModel(models.Model):
    id_openpattern = models.ForeignKey(
        openPatternModel, on_delete=models.CASCADE)
    day = models.DateField(auto_now_add=True)


class reservationModel(models.Model):
    id_user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    id_timetable = models.ForeignKey(
        timeTableModel, on_delete=models.CASCADE)
    day = models.DateField(auto_now_add=True)
