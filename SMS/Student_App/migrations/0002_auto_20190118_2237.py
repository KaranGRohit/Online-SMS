# Generated by Django 2.1.4 on 2019-01-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='SName',
            new_name='FName',
        ),
        migrations.AddField(
            model_name='student',
            name='SAge',
            field=models.IntegerField(default=18),
        ),
    ]
