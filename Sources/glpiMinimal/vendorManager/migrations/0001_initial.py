# Generated by Django 2.1.1 on 2018-09-30 19:34

from django.db import migrations, models
import django.db.models.deletion


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
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='command',
            name='commandState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorManager.CommandState'),
        ),
        migrations.AddField(
            model_name='command',
            name='vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vendorManager.Vendor'),
        ),
    ]
