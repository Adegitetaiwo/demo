# Generated by Django 3.2.6 on 2021-09-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books_Archive', '0003_books_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='verified',
            field=models.BooleanField(default=True),
        ),
    ]