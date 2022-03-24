# Generated by Django 4.0.2 on 2022-03-24 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_service'),
        ('users', '0002_customuser_date_created_customuser_is_project_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_project_user',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_supporter',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='providing',
            field=models.ManyToManyField(blank=True, null=True, related_name='providers', to='projects.Service'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
