# Generated by Django 3.0.5 on 2020-04-21 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showTimesApp', '0002_auto_20200421_2114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(blank=True, max_length=2500),
        ),
    ]
