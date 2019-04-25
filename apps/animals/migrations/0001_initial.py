# Generated by Django 2.2 on 2019-04-23 18:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('organizations', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('species', models.CharField(max_length=128)),
                ('breed', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField()),
                ('size', models.CharField(max_length=128)),
                ('social', models.CharField(max_length=128)),
                ('accommodation', models.CharField(max_length=256)),
                ('tag', models.CharField(max_length=128)),
                ('microchip', models.CharField(max_length=128)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization')),
            ],
        ),
    ]
