# Generated by Django 4.0.2 on 2022-03-22 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_location_project_urgent'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default='1 April 2022'),
            preserve_default=False,
        ),
    ]
