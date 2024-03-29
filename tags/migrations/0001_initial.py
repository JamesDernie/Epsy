# Generated by Django 2.0.4 on 2018-05-01 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='links.Link')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('link', 'name')},
        ),
    ]
