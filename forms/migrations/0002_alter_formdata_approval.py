# Generated by Django 5.0.6 on 2024-06-24 20:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("forms", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formdata",
            name="approval",
            field=models.BooleanField(default=False),
        ),
    ]
