# Generated by Django 5.1 on 2024-09-18 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0003_telegramuser"),
    ]

    operations = [
        migrations.AlterField(
            model_name="telegramuser",
            name="telegram_id",
            field=models.IntegerField(db_index=True),
        ),
    ]
