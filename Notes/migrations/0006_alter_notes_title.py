# Generated by Django 5.0 on 2024-05-27 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Notes", "0005_alter_dropdown_drop_down_alter_notes_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notes",
            name="title",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
