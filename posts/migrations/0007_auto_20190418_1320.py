# Generated by Django 2.1.7 on 2019-04-18 04:20

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190418_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(upload_to=''),
        ),
    ]
