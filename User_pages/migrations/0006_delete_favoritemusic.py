# Generated by Django 4.1.1 on 2023-06-11 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User_pages', '0005_remove_favoritemusic_musics'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavoriteMusic',
        ),
    ]
