# Generated by Django 3.2 on 2021-04-15 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20210415_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('?', '?'), ('', '')], default='', max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Combination_Fur',
            field=models.CharField(blank=True, default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Hectare',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Hectare_Squirrel_Number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
