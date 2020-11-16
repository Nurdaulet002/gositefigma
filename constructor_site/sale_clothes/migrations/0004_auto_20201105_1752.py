# Generated by Django 3.1 on 2020-11-05 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale_clothes', '0003_auto_20201105_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='bag',
        ),
        migrations.AddField(
            model_name='good',
            name='color',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='good',
            name='counter',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='good',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='good',
            name='sizes',
            field=models.CharField(max_length=30, null=True),
        ),
    ]