# Generated by Django 4.1.2 on 2022-10-08 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("issues", "0002_auto_20221006_1938"),
    ]

    operations = [
        migrations.AddField(
            model_name="issue",
            name="created_on",
            field=models.DateField(blank=True, null=True),
        ),
    ]
