# Generated by Django 4.0.5 on 2022-06-04 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pywvApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]