# Generated by Django 4.1.7 on 2023-05-30 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recipe", "0005_recipe_difficulty"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="difficulty",
            field=models.IntegerField(default=1),
        ),
    ]
