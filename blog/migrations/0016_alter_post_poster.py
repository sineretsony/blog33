# Generated by Django 4.2.7 on 2023-12-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_post_poster_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='poster',
            field=models.URLField(default='https://png.pngtree.com.jpg', verbose_name='Постер'),
        ),
    ]
