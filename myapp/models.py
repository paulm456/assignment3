from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings





# Custom User model with additional fields
class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    pass


class Booking(models.Model):
    BOOKING_CHOICES = [
        ('sr', 'Standard Room'),
        ('js', 'Junior Suite'),
        ('ms', 'Master Suite'),
        ('spa', 'Spa'),
        ('golf', 'Golf'),
    ]

    
    booking_type = models.CharField(max_length=10, choices=BOOKING_CHOICES)
    pay_now = models.DecimalField(max_digits=7, decimal_places=2)
    checkin_date = models.DateField()
    checkout_date = models.DateField()
    guests = models.PositiveIntegerField()
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer.username} - {self.get_booking_type_display()} ({self.checkin_date} to {self.checkout_date})"
    


