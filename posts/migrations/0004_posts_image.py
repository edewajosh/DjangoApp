# Generated by Django 2.0.1 on 2018-01-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]