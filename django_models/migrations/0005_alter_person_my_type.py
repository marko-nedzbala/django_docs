# Generated by Django 5.1.7 on 2025-03-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_models', '0004_person_my_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='my_type',
            field=models.CharField(blank=True, choices=[('Type01', 'Type01'), ('Type02', 'Type02'), ('Type03', 'Type03')], max_length=8),
        ),
    ]
