# Generated by Django 3.1.6 on 2021-04-09 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0039_remove_productrecommendation_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='productrecommendation',
            name='score',
            field=models.FloatField(default=1.0),
            preserve_default=False,
        ),
    ]
