# Generated by Django 4.0.5 on 2022-06-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='table_id',
            field=models.IntegerField(),
        ),
    ]
