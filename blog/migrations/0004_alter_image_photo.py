# Generated by Django 4.2.1 on 2023-05-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_image_id_alter_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to='images'),
        ),
    ]
