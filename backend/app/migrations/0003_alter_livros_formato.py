# Generated by Django 5.0.5 on 2024-05-30 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_rename_anopublicação_livros_anopublicacao_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="livros",
            name="formato",
            field=models.CharField(
                choices=[("Ebook", "Ebook"), ("Fisico", "Fisico")], max_length=20
            ),
        ),
    ]