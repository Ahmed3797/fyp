# Generated by Django 4.2.5 on 2024-05-06 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0009_user_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_answer',
            name='user',
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Spoofing_detection', models.IntegerField(default=0)),
                ('copy_pasting', models.IntegerField(default=0)),
                ('tab_changing', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_answers', models.ManyToManyField(related_name='reports', to='company.user_answer')),
            ],
        ),
    ]
