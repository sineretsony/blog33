# Generated by Django 4.2.7 on 2023-12-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_remove_userprofile_email_remove_userprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.ImageField(default='default_poster.jpg', upload_to='posters/', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(default='base.jpg', upload_to='avatars/', verbose_name='Аватар'),
        ),
    ]
