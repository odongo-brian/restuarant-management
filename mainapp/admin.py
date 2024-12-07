from django.contrib import admin
from .models import Room, Booking

# Register your models here.
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'room_type', 'price_per_night', 'is_available')  # Shows room details
    search_fields = ('room_number', 'room_type')    # Allows searching rooms by room number or type
    list_filter = ('is_available',)  # Filters rooms based on availability

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'start_date', 'end_date', 'status' )
    list_filter = ('status', 'room', 'start_date', 'end_date')
    search_fields = ('user__username', 'room__room_number')

