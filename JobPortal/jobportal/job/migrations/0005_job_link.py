# Generated by Django 2.2 on 2021-05-02 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0004_appliedjobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
