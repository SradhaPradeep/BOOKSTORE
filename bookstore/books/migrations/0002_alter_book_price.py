# Generated by Django 4.2.5 on 2023-09-13 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=3, max_digits=5),
        ),
    ]
