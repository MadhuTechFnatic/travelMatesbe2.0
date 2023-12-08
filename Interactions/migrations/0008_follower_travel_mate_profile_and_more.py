# Generated by Django 4.2.3 on 2023-11-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Interactions', '0007_follower_follower_name_follower_travel_mate_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='follower',
            name='travel_mate_profile',
            field=models.URLField(default='d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tripcomment',
            name='travel_mate_profile',
            field=models.URLField(default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='triprequest',
            name='travel_mate_profile',
            field=models.URLField(default='1'),
            preserve_default=False,
        ),
    ]