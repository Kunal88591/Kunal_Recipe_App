# Generated by Django 5.0.7 on 2024-12-17 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Kunal_Recipe_App", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipe",
            name="receipe_image",
            field=models.ImageField(upload_to=""),
        ),
    ]
