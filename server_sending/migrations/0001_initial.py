# Generated by Django 4.1 on 2022-08-09 08:54

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                (
                    "tel_number",
                    models.IntegerField(
                        validators=[
                            django.core.validators.RegexValidator(regex="^7\\d{10}$")
                        ]
                    ),
                ),
                ("mobile_code", models.IntegerField()),
                ("tag", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Massage",
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
                ("pub_date", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("S", "Send"), ("N", "No send")],
                        default="N",
                        max_length=1,
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="clients",
                        to="server_sending.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sending",
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
                ("star", models.DateTimeField()),
                ("stop", models.DateTimeField()),
                ("massage", models.TextField()),
                (
                    "status",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="statuses",
                        to="server_sending.massage",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tags",
                        to="server_sending.client",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="massage",
            name="sending",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sendings",
                to="server_sending.sending",
            ),
        ),
    ]