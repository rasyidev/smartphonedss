# Generated by Django 3.1.6 on 2021-03-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_smartphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smartphone',
            name='battery',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='camera',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='cpu',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='memory',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='smartphone',
            name='ram',
            field=models.CharField(max_length=255),
        ),
    ]
