# Generated by Django 2.2.3 on 2019-07-18 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageuploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageupload',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]