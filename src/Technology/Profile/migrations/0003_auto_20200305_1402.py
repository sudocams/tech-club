# Generated by Django 2.2 on 2020-03-05 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0002_auto_20200304_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applications',
            name='admin_no',
            field=models.CharField(max_length=40),
        ),
    ]