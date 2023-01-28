# Generated by Django 4.1.5 on 2023-01-26 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("business", "ビジネス"),
                            ("life", "生活"),
                            ("other", "その他"),
                        ],
                        max_length=100,
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="SampleModel",
        ),
    ]
