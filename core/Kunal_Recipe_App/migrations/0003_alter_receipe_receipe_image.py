# Generated by Django 5.0.7 on 2024-12-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Kunal_Recipe_App", "0002_alter_receipe_receipe_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receipe",
            name="receipe_image",
            field=models.ImageField(upload_to="receipe"),
        ),
    ]