# Generated by Django 4.2.5 on 2024-05-06 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0014_alter_report_user_answers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='report',
            name='user_answers',
        ),
        migrations.AddField(
            model_name='report',
            name='user_answers',
            field=models.ManyToManyField(related_name='reports', to='company.user_answer'),
        ),
    ]
