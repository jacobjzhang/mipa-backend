# Generated by Django 2.1.5 on 2019-01-21 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='current_score',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='code',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='hint',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='hintImage',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='options',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='questionImage',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
