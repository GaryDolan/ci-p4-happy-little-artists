# Generated by Django 3.2 on 2024-01-01 17:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a class title', max_length=100, unique=True)),
                ('description', models.CharField(blank=True, help_text='Enter a brief class description', max_length=200, null=True)),
                ('start_date', models.DateTimeField(help_text='Select the start date')),
                ('end_date', models.DateTimeField(help_text='Select the end date')),
                ('duration', models.DurationField(help_text='Enter the class duration')),
                ('location', models.CharField(help_text='Enter class location', max_length=20)),
                ('age_group', models.IntegerField(choices=[(0, '5-7'), (1, '8-10')])),
                ('bookings_count', models.IntegerField(default=0)),
                ('max_bookings', models.IntegerField(default=20)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.IntegerField(choices=[(0, 'Not Paid'), (1, 'Paid')])),
                ('admin_notes', models.TextField(help_text='Enter booking notes here')),
                ('child_name', models.CharField(help_text="Enter the child's name", max_length=20)),
                ('contact_number', models.CharField(help_text='Enter the contact number', max_length=20)),
                ('emg_contact_number', models.CharField(help_text='Enter the emergency contact number', max_length=20)),
                ('art_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='bookings.artclass')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
    ]
