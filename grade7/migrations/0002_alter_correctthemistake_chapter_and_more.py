# Generated by Django 4.1 on 2023-08-24 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('grade7', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='correctthemistake',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade7.chapter'),
        ),
        migrations.AlterField(
            model_name='makequestions',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade7.chapter'),
        ),
        migrations.AlterField(
            model_name='multiples',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade7.chapter'),
        ),
        migrations.AlterField(
            model_name='paragraphs',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade7.chapter'),
        ),
        migrations.AlterField(
            model_name='text',
            name='chapter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='texts', to='grade7.chapter'),
        ),
        migrations.AlterField(
            model_name='textquestion',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade7.text'),
        ),
        migrations.AlterField(
            model_name='tfquestions',
            name='text',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grade7.text'),
        ),
    ]
