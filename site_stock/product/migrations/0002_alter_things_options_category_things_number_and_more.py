# Generated by Django 4.2 on 2023-04-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="things",
            options={"ordering": ("name",), "verbose_name_plural": "Things"},
        ),
        migrations.AddField(
            model_name="category",
            name="things_number",
            field=models.IntegerField(default=0, verbose_name="Things number"),
        ),
        migrations.AddIndex(
            model_name="things",
            index=models.Index(fields=["name"], name="things_names_idx"),
        ),
    ]
