# Generated by Django 3.1.6 on 2021-04-07 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_recomendation'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Recomendation',
            new_name='ProductRecommendation',
        ),
    ]
