# Generated by Django 3.0.5 on 2020-05-04 12:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sample_relations', '0002_auto_20200504_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='multi',
            name='publicatioon_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
