from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class ArtClass(models.Model):
    # Tuples to control age and duration choices
    AGE_GROUP_CHOICES = (('5-7', '5-7 years old'), ('8-10', '8-10 years old'),)
    DURATION_CHOICES = (('1', '1 hour'), ('1.5', '1.5 hours'), ('2', '2 hours'),)

    title = models.CharField(max_length=100, unique=True, help_text='Enter a class title')
    description = models.CharField(max_length=200, help_text='Enter a brief class description', null=True, blank=True)
    start_date = models.DateField(help_text='Select the start date')
    end_date = models.DateField(help_text='Select the end date')
    start_time = models.TimeField(help_text='Select the start time')
    duration = models.CharField(max_length=10,choices=DURATION_CHOICES, help_text='Enter the class duration')
    location = models.CharField(max_length=20, help_text='Enter class location')
    age_group = models.CharField(max_length=10,choices=AGE_GROUP_CHOICES)
    bookings_count = models.IntegerField(default=0)
    max_bookings = models.IntegerField(default=20)

    def __str__(self):
        return self.title

class Booking(models.Model):
    # Tuple to control the booking payment status
    PAYMENT_STATUS_CHOICES = ((0, "Not Paid"), (1, "Paid"),)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    date_created = models.DateTimeField(auto_now_add=True)
    payment_status = models.IntegerField(choices=PAYMENT_STATUS_CHOICES, default=0 )
    art_class = models.ForeignKey(ArtClass, on_delete=models.CASCADE, related_name="bookings")
    admin_notes = models.TextField(help_text='Enter booking notes here', blank=True)
    child_name = models.CharField(max_length=20, help_text="Enter name (letters only)")
    contact_number = models.CharField(max_length=20, help_text="Enter number in the format XXX XXX XXXX")
    emg_contact_name = models.CharField(max_length=20, help_text="Enter name (letters only)")
    emg_contact_number = models.CharField(max_length=20, help_text="Enter number in the format XXX XXX XXXX")


    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"{self.owner.username}'s Booking for {self.art_class}"

# Use the post_save signal from the booking model to set the booking count of the associated art class
@receiver(post_save, sender=Booking)
def add_booking_to_class(sender, instance, **kwargs):
    # Increase the bookings_count of the associated ArtClass
    art_class = instance.art_class
    art_class.bookings_count += 1
    # only save the booking count
    art_class.save(update_fields=['bookings_count'])

 # Use the post_delete signal from the booking model to set the booking count of the associated art class
@receiver(post_delete, sender=Booking)
def remove_booking_from_class(sender, instance, **kwargs):
    # Decrease the bookings_count of the associated ArtClass
    art_class = instance.art_class
    remaining_bookings_count = Booking.objects.filter(art_class=art_class).count()
    art_class.bookings_count = remaining_bookings_count
    # only save the booking count
    art_class.save(update_fields=['bookings_count'])
    