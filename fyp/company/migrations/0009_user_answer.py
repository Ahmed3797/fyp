# Generated by Django 4.2.5 on 2024-03-19 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('company', '0008_alter_interview_end_date_alter_interview_start_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_answer', models.CharField(max_length=1000)),
                ('question_inter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
