# Generated by Django 2.2.4 on 2019-09-09 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(default='test'),
            preserve_default=False,
        ),
    ]
