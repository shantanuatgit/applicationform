# Generated by Django 2.0.2 on 2020-06-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googleform', '0003_auto_20200620_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvmodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
