# Generated by Django 2.2.5 on 2020-07-13 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetstatement',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='incomestatement',
            name='price',
            field=models.DecimalField(decimal_places=4, max_digits=14, null=True),
        ),
    ]
