# Generated by Django 2.2 on 2019-05-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0003_auto_20190507_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breed',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
