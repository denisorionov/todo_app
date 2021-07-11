# Generated by Django 3.2.4 on 2021-07-10 19:51

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('task_list', '0005_historicaltask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicaltask',
            name='due_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, verbose_name='Срок выполнения'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(blank=True, verbose_name='Срок выполнения'),
        ),
        migrations.AlterField(
            model_name='task',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
