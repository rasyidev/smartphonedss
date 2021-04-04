# Generated by Django 3.1.6 on 2021-03-31 03:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_delete_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.CharField(max_length=255)),
                ('rank', models.IntegerField()),
                ('price', models.IntegerField()),
                ('url_product', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('ram', models.CharField(max_length=255)),
                ('cpu', models.CharField(max_length=255)),
                ('storage', models.CharField(max_length=255)),
                ('battery', models.CharField(max_length=255)),
                ('url_specs', models.CharField(max_length=255)),
                ('img_url', models.CharField(max_length=255)),
                ('main_cam', models.CharField(max_length=255)),
                ('selfie_cam', models.CharField(max_length=255)),
                ('smartphone_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.smartphone')),
            ],
        ),
    ]
