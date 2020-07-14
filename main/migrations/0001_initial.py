# Generated by Django 2.2.5 on 2020-07-13 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=150)),
                ('item', models.CharField(choices=[('A', 'Asset'), ('L', 'Loan')], default='A', max_length=2)),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='IncomeStatement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=150)),
                ('item', models.CharField(choices=[('S', 'Sales'), ('P', 'Profit')], default='S', max_length=2)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
