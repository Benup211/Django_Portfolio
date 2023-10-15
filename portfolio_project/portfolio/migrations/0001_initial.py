# Generated by Django 4.2.4 on 2023-10-15 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
                ('experience', models.PositiveIntegerField()),
                ('icon', models.CharField(max_length=200)),
            ],
        ),
    ]