# Generated by Django 2.1.1 on 2018-09-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Command',
            fields=[
                ('ref', models.UUIDField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='CommandState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('adress', models.CharField(max_length=512)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('comment', models.TextField(null=True)),
            ],
        ),
    ]