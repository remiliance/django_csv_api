# Generated by Django 3.2.7 on 2021-09-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airport', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='traffic',
            name='TERMINAL',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]