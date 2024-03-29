# Generated by Django 4.0.1 on 2022-01-13 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksAPIApp', '0002_alter_category_options_book_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=11)),
            ],
        ),
    ]
