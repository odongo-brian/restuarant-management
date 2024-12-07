# booking/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from .forms import BookingForm, BookingStatusForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

# View to list available rooms
def room_list(request):
    rooms = Room.objects.filter(is_available=True)  # Filter rooms that are available
    return render(request, 'room_list.html', {'rooms': rooms})

# View to handle booking a room (for users)
@login_required
def book_room(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            room.available = False  # Mark room as unavailable
            room.save()
            return redirect('booking_success')
    else:
        form = BookingForm(initial={'room': room})
    return render(request, 'book_room.html', {'form': form, 'room': room})

# View for a successful booking
def booking_success(request):
    return render(request, 'booking_success.html')

# Admin view to see all bookings
@login_required
def admin_booking_list(request):
    if not request.user.is_staff:
        return redirect('home')  # Redirect non-admin users to home page
    bookings = Booking.objects.all()
    return render(request, 'admin_booking_list.html', {'bookings': bookings})

# Admin view to accept or decline a booking
@login_required
def update_booking_status(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.user.is_staff:
        if request.method == 'POST':
            form = BookingStatusForm(request.POST, instance=booking)
            if form.is_valid():
                form.save()
                if booking.status == 'Accepted':
                    booking.room.available = False  # Mark room as unavailable if booking is accepted
                    booking.room.save()
                else:
                    booking.room.available = True  # Mark room as available if booking is declined
                    booking.room.save()
                return redirect('booking:admin_booking_list')
        else:
            form = BookingStatusForm(instance=booking)
        return render(request, 'update-booking_status.html', {'form': form, 'booking': booking})
    return redirect('home')

@login_required
def user_bookings(request):
    # Get the bookings for the currently logged-in user
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'user_booking.html', {'bookings': bookings})


def base(request):
    return render(request, 'base.html')

def contact(request):
    return render(request, 'contact.html')