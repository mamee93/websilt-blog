# Generated by Django 3.0.6 on 2020-06-26 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0018_auto_20200626_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='brand',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Brand', to='ad.Brand'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(limit_choices_to={'main_category__isnull': True}, on_delete=django.db.models.deletion.CASCADE, related_name='ad_category', to='ad.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='main_category',
            field=models.ForeignKey(blank=True, limit_choices_to={'main_category__isnull': None}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maincategory', to='ad.Category'),
        ),
    ]
