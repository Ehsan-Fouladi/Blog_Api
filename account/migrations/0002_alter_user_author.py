# Generated by Django 5.1 on 2024-08-12 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='author',
            field=models.BooleanField(default=True),
        ),
    ]
