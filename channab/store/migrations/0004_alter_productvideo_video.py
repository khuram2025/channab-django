# Generated by Django 4.0.5 on 2022-07-05 12:24

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_productvideo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvideo',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
    ]