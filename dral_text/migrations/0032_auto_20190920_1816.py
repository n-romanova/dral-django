# Generated by Django 2.2.3 on 2019-09-20 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dral_text', '0031_visualisation_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visualisation',
            name='short_description',
            field=models.TextField(blank=True, help_text='Short description on top of the visualisation.\n        Ideally one sentence. You can insert links to keep things concise.\n        Formatting is done by using markdown syntax\n        (https://daringfireball.net/projects/markdown/syntax)\n        '),
        ),
        migrations.AlterField(
            model_name='visualisation',
            name='visibility',
            field=models.CharField(choices=[('dev', 'Development'), ('liv', 'Live')], default='dev', help_text='If "Live" the viz is publicly visible', max_length=30),
        ),
    ]
