# Generated by Django 4.1 on 2023-08-24 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade12', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.SmallIntegerField(choices=[(1, 'chapter one'), (2, 'chapter Two'), (3, 'chapter Three'), (4, 'chapter Four'), (5, 'chapter Five'), (6, 'chapter Six'), (7, 'chapter Seven'), (8, 'chapter Eight'), (9, 'chapter Nine'), (10, 'chapter Ten'), (11, 'chapter Eleven'), (12, 'chapter Twelve')], unique=True),
        ),
    ]