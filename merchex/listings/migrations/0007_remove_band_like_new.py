# Generated by Django 4.0.6 on 2022-08-03 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_band_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='like_new',
        ),
    ]
