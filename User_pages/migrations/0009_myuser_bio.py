# Generated by Django 4.1.1 on 2023-06-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User_pages', '0008_remove_favoritemusic_sound_favoritemusic_musics'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bio',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
