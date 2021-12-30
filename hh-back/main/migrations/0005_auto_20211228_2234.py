# Generated by Django 3.2.9 on 2021-12-28 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_resumes_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resumes',
            name='job_experience',
            field=models.IntegerField(default=0, verbose_name='Опыт работы в годах'),
        ),
        migrations.AlterField(
            model_name='resumes',
            name='study_degree',
            field=models.CharField(max_length=200, null=True, verbose_name='Образование'),
        ),
    ]
