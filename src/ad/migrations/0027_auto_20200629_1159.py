# Generated by Django 3.0.6 on 2020-06-29 07:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0026_auto_20200626_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='category',
            field=models.ForeignKey(limit_choices_to={'main_category__isnull': True}, on_delete=django.db.models.deletion.CASCADE, related_name='ad_category', to='ad.Category'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='condition',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Like New', 'Like New'), ('Good Condition', 'Good Condition'), ('Bad Condition', 'Bad Condition')], max_length=15, null=True),
        ),
    ]
