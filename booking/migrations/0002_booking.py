# Generated by Django 3.2 on 2021-04-22 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theater', '0002_auto_20210422_2328'),
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booked_on', models.DateTimeField(auto_now_add=True)),
                ('ShowTiming', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='theater.showtiming')),
                ('booked_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='booking.user')),
            ],
        ),
    ]
