# Generated by Django 4.2.6 on 2023-10-30 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='workers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350)),
                ('img', models.ImageField(upload_to='pics')),
                ('des', models.TextField()),
            ],
        ),
    ]
