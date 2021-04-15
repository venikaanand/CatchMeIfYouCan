# Generated by Django 3.2 on 2021-04-15 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20210415_0059'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squirrel',
            fields=[
                ('Latitude', models.FloatField(null=True)),
                ('Longitude', models.FloatField(null=True)),
                ('Unique_Squirrel_ID', models.CharField(max_length=14, primary_key=True, serialize=False)),
                ('Hectare', models.CharField(max_length=200, null=True)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', max_length=14, null=True)),
                ('Date', models.DateField(null=True)),
                ('Hectare_Squirrel_Number', models.CharField(max_length=200, null=True)),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('?', '?'), ('', '')], default='', max_length=14, null=True)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnammon', 'Cinnammon'), ('', '')], default='', max_length=14, null=True)),
                ('Highlight_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnammon', 'Cinnammon'), ('White', 'White'), ('Black, Cinnammon', 'Black, Cinnammon'), ('Black, White', 'Black, White'), ('Black, Cinnammon, White', 'Black, Cinnammon, White'), ('Cinammon, White', 'Cinammon, White'), ('Gray, Black', 'Gray, Black'), ('Black, White', 'Black, White'), ('Gray, White', 'Gray, White'), ('', '')], default='', max_length=200, null=True)),
                ('Combination_Fur', models.CharField(default='', max_length=200, null=True)),
                ('Color_Notes', models.CharField(blank=True, max_length=200, null=True)),
                ('Location', models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane'), ('', '')], default='', max_length=200, null=True)),
                ('Above_Ground_Sighter_Measurement', models.CharField(blank=True, max_length=200, null=True)),
                ('Specific_Location', models.CharField(blank=True, max_length=200, null=True)),
                ('Running', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Chasing', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Climbing', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Eating', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Other_Activities', models.CharField(blank=True, max_length=200, null=True)),
                ('Kuks', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Quaas', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Moans', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Tail_Flags', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Tail_Twitches', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Approaches', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Foraging', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Runs_From', models.CharField(choices=[('TRUE', 'true'), ('FALSE', 'false')], default='FALSE', max_length=200, null=True)),
                ('Other_Interactions', models.CharField(blank=True, max_length=200, null=True)),
                ('Lat_Long', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='squirrelmodel',
            name='Indifferent',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Indifferent', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Above_Ground_Sighter_Measurement',
            field=models.CharField(blank=True, help_text='Above Ground Sighter Measurement', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Age',
            field=models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('Unknown', '?'), ('', '')], default='', help_text='Age', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Approaches',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Approaches', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Chasing',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Chasing', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Climbing',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Climbing', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Color_Notes',
            field=models.CharField(blank=True, help_text='Color notes', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Combination_Fur',
            field=models.CharField(default='+', help_text='Combination of Primary and Highlight Color', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Date',
            field=models.DateField(help_text='Date', null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Eating',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Eating', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Foraging',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Foraging', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Hectare',
            field=models.CharField(help_text='Hectare', max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Hectare_Squirrel_Number',
            field=models.CharField(help_text='Hectare Squirrel Number', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Highlight_Fur_Color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnammon', 'Cinnammon'), ('White', 'White'), ('Black, Cinnammon', 'Black, Cinnammon'), ('Black, White', 'Black, White'), ('Black, Cinnammon, White', 'Black, Cinnammon, White'), ('Cinnammon, White', 'Cinammon, White'), ('Gray, Black', 'Gray, Black'), ('Black, White', 'Black, White'), ('Gray, White', 'Gray, White'), ('', '')], default='', help_text='Highlight Fur Color', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Kuks',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Kuks', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Lat_Long',
            field=models.CharField(blank=True, help_text='Lat/Long', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Latitude',
            field=models.FloatField(help_text='X', null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Location',
            field=models.CharField(blank=True, choices=[('Above Ground', 'Above Ground'), ('Ground Plane', 'Ground Plane'), ('', '')], default='', help_text='Location', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Longitude',
            field=models.FloatField(help_text='Y', null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Moans',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Moans', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Other_Activities',
            field=models.CharField(blank=True, help_text='Other Activities', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Other_Interactions',
            field=models.CharField(blank=True, help_text='Other Interactions', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Primary_Fur_Color',
            field=models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Black', 'Black'), ('Cinnammon', 'Cinnammon'), ('', '')], default='', help_text='Primary Fur Color', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Quaas',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Quaas', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Running',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Running', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Runs_From',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Runs from', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Shift', max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Specific_Location',
            field=models.CharField(blank=True, help_text='Specific Location', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Tail_Flags',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Tail flags', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Tail_Twitches',
            field=models.CharField(choices=[('true', 'true'), ('false', 'false')], default='false', help_text='Tail twitches', max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='squirrelmodel',
            name='Unique_Squirrel_ID',
            field=models.CharField(help_text='Unique Squirrel ID', max_length=14, primary_key=True, serialize=False),
        ),
    ]