# Generated by Django 4.0.2 on 2022-04-12 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music2', '0003_alter_rating_id_alter_rating_song_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Song',
        ),
    ]
