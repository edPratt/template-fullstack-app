# Generated by Django 2.0 on 2018-05-24 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
