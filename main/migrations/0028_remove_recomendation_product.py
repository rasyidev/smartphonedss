# Generated by Django 3.1.6 on 2021-04-07 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20210407_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recomendation',
            name='product',
        ),
    ]
