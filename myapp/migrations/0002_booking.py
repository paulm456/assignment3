# Generated by Django 5.2 on 2025-04-08 16:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_type', models.CharField(choices=[('sr', 'Standard Room'), ('js', 'Junior Suite'), ('ms', 'Master Suite'), ('spa', 'Spa'), ('golf', 'Golf')], max_length=10)),
                ('pay_now', models.DecimalField(decimal_places=2, max_digits=7)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('guests', models.PositiveIntegerField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
