# Generated by Django 4.2.7 on 2023-12-06 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_comment_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_name', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'verbose_name': 'Подписчик на рассылку',
                'verbose_name_plural': 'Подписчики на рассылку',
            },
        ),
    ]
