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
]