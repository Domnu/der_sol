# Generated by Django 5.0.1 on 2024-01-19 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artik", "0004_remove_pageweb_contenu_pageweb_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pageweb",
            name="url",
            field=models.URLField(max_length=255),
        ),
    ]
