# Generated by Django 3.1 on 2021-03-27 11:13

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0006_auto_20210320_0958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='entry_text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
