# Generated by Django 4.0.4 on 2022-05-27 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Libreria', '0002_alter_libro_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='isbn',
            field=models.IntegerField(),
        ),
    ]
