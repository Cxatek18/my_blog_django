# Generated by Django 3.2 on 2022-04-20 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='created_at',
            new_name='created_data',
        ),
    ]