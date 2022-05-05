# Generated by Django 3.2.6 on 2021-08-21 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooksArchive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('file', models.FileField(upload_to='')),
                ('author', models.CharField(max_length=250)),
                ('volume', models.CharField(blank=True, max_length=250)),
            ],
            options={
                'verbose_name_plural': 'Books Archive',
            },
        ),
    ]