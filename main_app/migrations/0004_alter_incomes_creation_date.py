# Generated by Django 4.1.7 on 2023-02-28 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_incomes_description_alter_incomes_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incomes',
            name='creation_date',
            field=models.DateField(default=datetime.date(2023, 2, 28), verbose_name='Дата создания'),
        ),
    ]