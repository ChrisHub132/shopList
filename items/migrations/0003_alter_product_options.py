# Generated by Django 4.2.7 on 2023-11-04 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_alter_category_options_product_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['id']},
        ),
    ]
