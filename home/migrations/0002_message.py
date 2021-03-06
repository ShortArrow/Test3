# Generated by Django 2.1.8 on 2019-06-02 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.homeModel')),
            ],
            options={
                'ordering': ('pub_date',),
            },
        ),
    ]
