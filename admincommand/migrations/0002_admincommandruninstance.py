# Generated by Django 3.2.10 on 2022-04-04 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("admincommand", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="AdminCommandRunInstance",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("command_name", models.CharField(max_length=200)),
                ("output", models.TextField()),
                ("has_exception", models.BooleanField()),
                ("executed_at", models.DateTimeField()),
                ("finished_at", models.DateTimeField(auto_now_add=True)),
                ("options", models.TextField(blank=True)),
                (
                    "runner_user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddIndex(
            model_name="admincommandruninstance",
            index=models.Index(
                fields=["command_name"], name="admincomman_command_d1d03a_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="admincommandruninstance",
            index=models.Index(
                fields=["runner_user"], name="admincomman_runner__3a6714_idx"
            ),
        ),
    ]
