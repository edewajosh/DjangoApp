# Generated by Django 2.0.1 on 2018-01-10 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='posts',
            name='author',
            field=models.CharField(default='Joshua Edewa', max_length=200),
            preserve_default=False,
        ),
    ]
