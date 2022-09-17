# Generated by Django 4.0.5 on 2022-07-05 12:26

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=embed_video.fields.EmbedVideoField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='ProductVideo',
        ),
    ]
