# booking/models.py

from django.db import models
from django.contrib.auth.models import User

# Room model: represents rooms in the restaurant
class Room(models.Model):
    room_number = models.CharField(max_length=100)
    room_type = models.TextField()
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.room_number

# Booking model: represents bookings made by users
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')],
        default='Pending'
    )

    def __str__(self):
        return f"Booking by {self.user.username} for {self.room.room_number}"
