# Generated by Django 3.0.6 on 2020-06-04 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0009_auto_20200605_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(limit_choices_to={'main_category__isnull': True}, on_delete=django.db.models.deletion.CASCADE, related_name='ad_category', to='ad.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maincategory', to='ad.Category'),
        ),
    ]