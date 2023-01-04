# Generated by Django 3.0.8 on 2020-08-27 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Anime', '0002_auto_20200827_0740'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadMovie',
            fields=[
                ('videoupload_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Anime.VideoUpload')),
            ],
            options={
                'verbose_name_plural': 'Upload Movies',
            },
            bases=('Anime.videoupload',),
        ),
        migrations.AlterModelOptions(
            name='uploadanime',
            options={'verbose_name_plural': 'Upload Animes'},
        ),
    ]
