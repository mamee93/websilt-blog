# Generated by Django 3.0.6 on 2020-06-04 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0014_auto_20200605_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='content',
            field=models.TextField(blank=True, null=0),
        ),
    ]