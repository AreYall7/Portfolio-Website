# Generated by Django 3.2 on 2021-04-25 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('proficiency', models.IntegerField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
    ]
