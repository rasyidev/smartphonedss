# Generated by Django 3.1.6 on 2021-04-07 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_cart_do_recommendation'),
    ]

    operations = [
        migrations.AddField(
            model_name='recomendation',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product'),
            preserve_default=False,
        ),
    ]
