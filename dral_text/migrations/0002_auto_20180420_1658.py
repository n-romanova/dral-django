# Generated by Django 2.0 on 2018-04-20 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dral_text', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='context',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
