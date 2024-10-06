# Generated by Django 5.1.1 on 2024-10-03 16:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0007_remove_professor_phone"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="examiners",
            field=models.ManyToManyField(
                related_name="examined_students", to="mainapp.professor"
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="mentor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="mentored_students",
                to="mainapp.professor",
            ),
        ),
    ]