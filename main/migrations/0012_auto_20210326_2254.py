# Generated by Django 3.1.6 on 2021-03-26 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20210326_2246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='smartphone',
            old_name='memory',
            new_name='storage',
        ),
    ]
