# Generated by Django 3.0.6 on 2020-06-26 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0025_auto_20200626_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(limit_choices_to={'main_category': True}, on_delete=django.db.models.deletion.CASCADE, related_name='ad_category', to='ad.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(blank=True, limit_choices_to={'main_category': None}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maincategory', to='ad.Category'),
        ),
    ]