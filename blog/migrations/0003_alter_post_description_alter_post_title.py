# Generated by Django 5.2 on 2025-04-12 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_description_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(default='Hola'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(verbose_name='Title'),
        ),
    ]
