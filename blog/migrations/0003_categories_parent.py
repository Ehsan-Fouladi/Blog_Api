# Generated by Django 5.1 on 2024-09-02 21:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='blog.categories'),
        ),
    ]
