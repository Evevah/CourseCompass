# Generated by Django 5.0.3 on 2024-04-09 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CourseCapp', '0007_section2_section3_section4'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='best_course',
            field=models.CharField(default='best', max_length=100),
        ),
    ]
