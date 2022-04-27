# Generated by Django 3.2.13 on 2022-04-27 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guestapp', '0007_previous_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='previous_reservation',
            name='pre_reservation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_reservation', to='guestapp.reservation'),
        ),
    ]
