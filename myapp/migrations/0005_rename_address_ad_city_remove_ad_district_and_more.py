# Generated by Django 4.2 on 2023-04-19 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_ad_image_ad_address_ad_district_ad_image1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='address',
            new_name='city',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='district',
        ),
        migrations.RemoveField(
            model_name='ad',
            name='state',
        ),
    ]
