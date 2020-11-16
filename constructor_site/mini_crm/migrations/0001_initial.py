# Generated by Django 3.1 on 2020-11-04 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management_site', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('counter', models.IntegerField(max_length=100)),
                ('size', models.CharField(max_length=4)),
                ('client_name', models.CharField(max_length=15)),
                ('phone', models.CharField(max_length=11)),
                ('is_payed', models.BooleanField(default=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('user_site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='management_site.usersite')),
            ],
        ),
    ]
