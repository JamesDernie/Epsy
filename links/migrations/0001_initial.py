# Generated by Django 2.0.4 on 2018-05-01 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, null=True)),
                ('icon', models.URLField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('comment', models.TextField(blank=True, max_length=1000, null=True)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='folders.Folder')),
            ],
        ),
    ]
