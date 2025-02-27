# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AdminCommand",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                )
            ],
            options={"abstract": False},
        ),
        migrations.AlterModelOptions(
            name="admincommand",
            options={
                "verbose_name": "Wadmin Command",
                "verbose_name_plural": "Wadmin Commands",
            },
        ),
    ]
