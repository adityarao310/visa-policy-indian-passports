# Generated by Django 2.0.4 on 2018-04-08 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visa_app', '0004_remove_country_country_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='country_image',
            field=models.ImageField(default='default.jpg', upload_to=None),
        ),
    ]
