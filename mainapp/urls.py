from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('contact/', views.contact, name='contact'),
    path('', views.room_list, name='room_list'),
    path('book_room/<int:room_id>/', views.book_room, name='book_room'),
    path('booking_success/', views.booking_success, name='booking_success'),
    path('admin/bookings/', views.admin_booking_list, name='admin_booking_list'),
    path('admin/update_booking/<int:booking_id>/', views.update_booking_status, name='update_booking_status'),
    path('rooms/', views.room_list, name='room_list'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('dashboard/', views.dashboard, name='user_dashboard'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('user/bookings/', views.user_bookings, name='user_bookings'),
    path('rooms/', views.room_list, name='room_list'),
    path('book/<int:room_id>/', views.book_room, name='book_room'),
]
