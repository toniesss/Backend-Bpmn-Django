# Generated by Django 4.1.7 on 2023-04-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_form_field_formfield_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formheader',
            name='form_key',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]