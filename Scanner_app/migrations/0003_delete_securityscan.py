# Generated by Django 5.1.6 on 2025-02-25 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Scanner_app", "0002_remove_securityscan_result_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="SecurityScan",
        ),
    ]
