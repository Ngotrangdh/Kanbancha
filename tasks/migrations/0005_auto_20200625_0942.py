# Generated by Django 3.0.7 on 2020-06-25 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20200623_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.TextField(default='todo'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('T', 'Todo'), ('P', 'Progress'), ('D', 'Done')], default='T', max_length=1),
        ),
    ]