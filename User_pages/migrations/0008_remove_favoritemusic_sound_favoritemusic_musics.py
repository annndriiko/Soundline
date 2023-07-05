# Generated by Django 4.1.1 on 2023-06-11 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_pages', '0007_alter_sound_file_alter_sound_image'),
        ('User_pages', '0007_favoritemusic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoritemusic',
            name='sound',
        ),
        migrations.AddField(
            model_name='favoritemusic',
            name='musics',
            field=models.ManyToManyField(to='Main_pages.sound'),
        ),
    ]
