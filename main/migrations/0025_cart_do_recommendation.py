# Generated by Django 3.1.6 on 2021-04-03 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_cart_productrecommendation_recomendation_smartphonecart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='do_recommendation',
            field=models.BooleanField(default=False),
        ),
    ]