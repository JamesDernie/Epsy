# Generated by Django 2.0.4 on 2018-04-22 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='profiles.Profile')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='tag',
            unique_together={('profile', 'name')},
        ),
    ]