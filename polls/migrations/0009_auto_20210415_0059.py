<<<<<<< HEAD
# Generated by Django 3.2 on 2021-04-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210415_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquirrelModel',
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
        migrations.DeleteModel(
            name='Squirrel',
        ),
        migrations.DeleteModel(
            name='Squirrel2',
        ),
    ]
=======
# Generated by Django 3.2 on 2021-04-15 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20210415_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='SquirrelModel',
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
        migrations.DeleteModel(
            name='Squirrel',
        ),
        migrations.DeleteModel(
            name='Squirrel2',
        ),
    ]
>>>>>>> d4b35acf0fc875078ef573a2c8764e055609208a
