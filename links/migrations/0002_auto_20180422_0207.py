# Generated by Django 2.0.4 on 2018-04-22 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link',
            old_name='folder',
            new_name='folders',
        ),
    ]
