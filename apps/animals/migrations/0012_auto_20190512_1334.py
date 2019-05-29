# Generated by Django 2.2 on 2019-05-12 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0011_animal_personality_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='kids_friendly',
            field=models.CharField(blank=True, choices=[('yes', 'Yes'), ('no', 'No'), ('only_females', 'Only females'), ('only_males', 'Only males'), ('only_young_kids', 'Only young kids'), ('only_old_kids', 'Only old kids'), ('both_young_and_old', 'Both young & old'), ('unknown', 'Unknown')], max_length=18, null=True),
        ),
    ]