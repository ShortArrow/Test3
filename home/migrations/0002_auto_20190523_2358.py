# Generated by Django 2.1.8 on 2019-05-23 14:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='illegalDayModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='openPatternModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ownerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('id_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='reservationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='roomGroupModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='roomModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('id_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ownerModel')),
            ],
        ),
        migrations.CreateModel(
            name='timeTableModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('price', models.IntegerField(default=0)),
                ('id_openpattern', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.openPatternModel')),
            ],
        ),
        migrations.AddField(
            model_name='roomgroupmodel',
            name='id_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.roomModel'),
        ),
        migrations.AddField(
            model_name='reservationmodel',
            name='id_timetable',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.timeTableModel'),
        ),
        migrations.AddField(
            model_name='reservationmodel',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='openpatternmodel',
            name='id_room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.roomModel'),
        ),
        migrations.AddField(
            model_name='illegaldaymodel',
            name='id_openpattern',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.openPatternModel'),
        ),
    ]
