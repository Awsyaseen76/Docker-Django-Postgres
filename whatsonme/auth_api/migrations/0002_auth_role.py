# Generated by Django 2.2 on 2019-08-05 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth',
            name='role',
            field=models.CharField(default='Member', max_length=128),
        ),
    ]