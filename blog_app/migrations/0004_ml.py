# Generated by Django 3.0.5 on 2020-11-21 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='ML',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('short_desc', models.CharField(default='', max_length=300)),
                ('slug', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]