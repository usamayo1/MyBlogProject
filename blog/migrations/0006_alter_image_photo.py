# Generated by Django 4.2.1 on 2023-05-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(auto_created=True, upload_to='images'),
        ),
    ]
