# Generated by Django 2.0.4 on 2018-05-01 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='links.Link'),
        ),
    ]
