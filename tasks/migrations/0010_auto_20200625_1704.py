# Generated by Django 3.0.7 on 2020-06-25 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_auto_20200625_1458'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assignor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='last_modified_by',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='last_modified_by', to=settings.AUTH_USER_MODEL),
        ),
    ]