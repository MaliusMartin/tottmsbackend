# Generated by Django 4.2.5 on 2023-11-14 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tottmsappbeta', '0023_alter_transferapplication_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='check_number',
            new_name='username',
        ),
    ]
