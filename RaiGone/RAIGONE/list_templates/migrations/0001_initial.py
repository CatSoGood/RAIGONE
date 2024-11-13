# Generated by Django 5.1.3 on 2024-11-10 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site', models.CharField(max_length=10)),
                ('rule', models.CharField(max_length=60)),
                ('user', models.CharField(max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
