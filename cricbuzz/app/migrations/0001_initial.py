# Generated by Django 2.2.28 on 2023-12-06 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='icc_bowling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('series', models.CharField(max_length=50)),
                ('player', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='app.player_info')),
            ],
        ),
        migrations.CreateModel(
            name='icc_batting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('series', models.CharField(max_length=50)),
                ('player', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='app.player_info')),
            ],
        ),
        migrations.CreateModel(
            name='icc_all_rounder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField()),
                ('rating', models.IntegerField()),
                ('series', models.CharField(max_length=50)),
                ('player', models.ForeignKey(auto_created=True, on_delete=django.db.models.deletion.CASCADE, to='app.player_info')),
            ],
        ),
    ]