# Generated by Django 2.0.2 on 2020-06-21 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googleform', '0007_auto_20200620_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cvmodel',
            name='file1',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
