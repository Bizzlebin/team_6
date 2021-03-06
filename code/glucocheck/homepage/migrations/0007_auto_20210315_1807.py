# Generated by Django 3.1.7 on 2021-03-15 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_carbohydrate_glucose_insulin_recordingcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carbohydrate',
            old_name='reading',
            new_name='carb_reading',
        ),
        migrations.RemoveField(
            model_name='glucose',
            name='categories',
        ),
        migrations.AddField(
            model_name='glucose',
            name='categories',
            field=models.ManyToManyField(to='homepage.RecordingCategory'),
        ),
        migrations.AlterField(
            model_name='recordingcategory',
            name='name',
            field=models.CharField(choices=[('fasting', 'Fasting'), ('before breakfast', 'Before Breakfast'), ('after breakfast', 'After Breakfast'), ('before lunch', 'Before Lunch'), ('after lunch', 'After Lunch'), ('snacks', 'Snacks'), ('before dinner', 'Before Dinner'), ('after dinner', 'After Dinner')], max_length=255, unique=True),
        ),
    ]
