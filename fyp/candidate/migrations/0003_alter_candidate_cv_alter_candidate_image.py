# Generated by Django 4.2.5 on 2023-10-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0002_remove_candidate_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cvs/'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
