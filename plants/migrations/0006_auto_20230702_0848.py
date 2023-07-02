# Generated by Django 3.2.19 on 2023-07-02 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_auto_20230702_0707'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='plantrecord',
            name='unique_plant_id',
        ),
        migrations.AddConstraint(
            model_name='plantrecord',
            constraint=models.UniqueConstraint(fields=('plant_number',), name='unique_plant_id'),
        ),
    ]