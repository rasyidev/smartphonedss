# Generated by Django 3.1.6 on 2021-03-31 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='battery',
        ),
        migrations.RemoveField(
            model_name='product',
            name='cpu',
        ),
        migrations.RemoveField(
            model_name='product',
            name='img_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='main_cam',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='ram',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rank',
        ),
        migrations.RemoveField(
            model_name='product',
            name='selfie_cam',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='product',
            name='smartphone_model',
        ),
        migrations.RemoveField(
            model_name='product',
            name='storage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url_product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='url_specs',
        ),
    ]
