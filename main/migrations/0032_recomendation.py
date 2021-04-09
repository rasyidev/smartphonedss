# Generated by Django 3.1.6 on 2021-04-07 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20210407_2253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recomendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.product')),
                ('smartphone_cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.smartphonecart')),
            ],
        ),
    ]
