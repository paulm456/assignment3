from django.urls import path

from . import views

app_name = "myapp"
urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_page, name="login"),
    path("rooms/", views.rooms_page, name="rooms"),
    path("spa/", views.spa_page, name="spa"),
    path("golf/", views.golf_page, name="golf"),
    path("dining/", views.dining_page, name="dining"),
    path("seasonal/", views.seasonal_page, name="seasonal"),
    path("membership/", views.membership_page, name="membership"),
    path("help/", views.help_page, name="help"),
    path('register/', views.register, name='register'),  # URL for the registration page
    path("bookings/", views.bookings_page, name="bookings"),
    path("logout/", views.logout_view, name="logout"),
    path("bookings/update/<int:booking_id>/", views.update_booking, name="update_booking"),
    path('bookings/delete/<int:booking_id>/', views.delete_booking, name='delete_booking'),
    path('bookings/all/', views.all_bookings, name='all_bookings'),

]