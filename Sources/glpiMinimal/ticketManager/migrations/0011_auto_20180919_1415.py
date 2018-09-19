# Generated by Django 2.1.1 on 2018-09-19 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userManager', '0003_auto_20180919_1336'),
        ('objectManager', '0007_auto_20180919_1415'),
        ('ticketManager', '0010_auto_20180919_1415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.UUIDField()),
                ('name', models.CharField(max_length=255)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userManager.User')),
                ('ticketObject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='objectManager.Object')),
            ],
        ),
        migrations.CreateModel(
            name='TicketMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('dateTime', models.DateTimeField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketManager.Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='TicketState',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='ticketState',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ticketManager.TicketState'),
        ),
    ]
