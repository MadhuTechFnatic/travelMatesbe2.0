# Generated by Django 4.2.6 on 2023-12-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TravelMates', '0008_alter_travelmate_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelmate',
            name='last_name',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
    ]
