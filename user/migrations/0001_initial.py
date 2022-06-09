# Generated by Django 4.0.1 on 2022-05-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='이메일')),
                ('name', models.CharField(max_length=150, null=True, verbose_name='이름')),
            ],
        ),
    ]