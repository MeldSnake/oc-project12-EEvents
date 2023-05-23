# Generated by Django 4.2.1 on 2023-05-23 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0002_contract_signed'),
        ('events', '0005_alter_event_contract_alter_event_support_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='contract',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='event', to='contracts.contract', verbose_name='Contract'),
        ),
    ]
