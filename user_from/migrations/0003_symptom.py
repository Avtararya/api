# Generated by Django 3.2.12 on 2022-05-11 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_from', '0002_delete_symptom'),
    ]

    operations = [
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptomname', models.TextField(max_length=100)),
            ],
        ),
    ]
