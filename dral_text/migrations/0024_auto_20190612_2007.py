# Generated by Django 2.1.5 on 2019-06-12 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dral_text', '0023_auto_20190327_0224'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Language',
            new_name='Text',
        ),
        migrations.RemoveIndex(
            model_name='sentence',
            name='dral_text_s_languag_13c74a_idx',
        ),
        migrations.RenameField(
            model_name='lemma',
            old_name='language',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='occurence',
            old_name='language',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='sentence',
            old_name='language',
            new_name='text',
        ),
        migrations.AlterUniqueTogether(
            name='occurence',
            unique_together={('chapter', 'lemma', 'cell_col', 'text')},
        ),
        migrations.AddIndex(
            model_name='sentence',
            index=models.Index(fields=['text'], name='dral_text_s_text_id_f9d98b_idx'),
        ),
    ]
