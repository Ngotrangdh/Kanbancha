# Generated by Django 3.0.7 on 2020-06-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_auto_20200625_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('T', 'Todo'), ('P', 'Progress'), ('D', 'Done')], max_length=1),
        ),
    ]