# Generated by Django 3.0.8 on 2020-08-31 13:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Anime', '0006_auto_20200830_1333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approved_date',
            new_name='approved_comment',
        ),
    ]
