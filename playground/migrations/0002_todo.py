# Generated by Django 4.2.2 on 2023-06-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('sno', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=122)),
                ('desc', models.CharField(max_length=500)),
                ('date_created', models.DateField()),
            ],
        ),
    ]
