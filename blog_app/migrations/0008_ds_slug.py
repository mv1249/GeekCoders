# Generated by Django 3.0.5 on 2020-11-21 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0007_auto_20201121_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='ds',
            name='slug',
            field=models.CharField(default='', max_length=100),
        ),
    ]
