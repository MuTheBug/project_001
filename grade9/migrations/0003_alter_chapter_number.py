# Generated by Django 4.1 on 2023-08-31 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grade9', '0002_chapter_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='number',
            field=models.CharField(choices=[('1a', 'chapter one activity'), ('1s', 'chapter one student'), ('2a', 'chapter two activity'), ('2s', 'chapter two student'), ('3a', 'chapter three activity'), ('3s', 'chapter three student'), ('4a', 'chapter four activity'), ('4s', 'chapter four student'), ('5a', 'chapter five activity'), ('5s', 'chapter five student'), ('6a', 'chapter six activity'), ('6s', 'chapter six student'), ('7a', 'chapter seven activity'), ('7s', 'chapter seven student'), ('8a', 'chapter eight activity'), ('8s', 'chapter eight student'), ('9a', 'chapter nine activity'), ('9s', 'chapter nine student'), ('10a', 'chapter ten activity'), ('10s', 'chapter ten student'), ('11a', 'chapter eleven activity'), ('11s', 'chapter eleven student'), ('12a', 'chapter twelve activity'), ('12s', 'chapter twelve student')], max_length=3, unique=True),
        ),
    ]
