# Generated by Django 4.2.5 on 2023-09-22 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0003_alter_book_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('items', models.ManyToManyField(to='books.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.cart')),
            ],
        ),
    ]
