# Generated by Django 5.0.3 on 2024-03-24 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CourseCapp', '0004_results'),
    ]

    operations = [
        migrations.RenameField(
            model_name='results',
            old_name='carrer',
            new_name='career',
        ),
    ]
