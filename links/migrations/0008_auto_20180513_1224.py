# Generated by Django 2.0.4 on 2018-05-13 12:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0007_auto_20180510_0444'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ('-created_at', 'id')},
        ),
        migrations.RemoveField(
            model_name='link',
            name='collection',
        ),
    ]