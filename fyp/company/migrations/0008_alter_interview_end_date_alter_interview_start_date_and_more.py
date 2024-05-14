# Generated by Django 4.2.5 on 2024-03-19 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_interview_schedulded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interview',
            name='end_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='interview',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.TextField(max_length=1000),
        ),
    ]
