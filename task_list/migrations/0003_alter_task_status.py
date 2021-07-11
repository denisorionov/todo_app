# Generated by Django 3.2.4 on 2021-07-03 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0002_alter_task_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('done', 'done'), ('in progress', 'in progress')], db_index=True, default='in progress', max_length=11, verbose_name='Статус задачи'),
        ),
    ]
