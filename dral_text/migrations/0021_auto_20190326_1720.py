# Generated by Django 2.1.5 on 2019-03-26 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dral_text', '0020_auto_20190211_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sentence',
            name='cell',
        ),
        migrations.AddField(
            model_name='language',
            name='slug',
            field=models.SlugField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='sentence',
            name='chapter',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='dral_text.Chapter'),
        ),
    ]
