# Generated by Django 4.0.5 on 2022-07-05 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_productvideo_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='store.productvideo'),
        ),
    ]
