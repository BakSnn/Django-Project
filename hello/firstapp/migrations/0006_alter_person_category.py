# Generated by Django 4.2.7 on 2023-12-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_alter_person_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='category',
            field=models.CharField(max_length=20),
        ),
    ]
