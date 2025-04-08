from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone

from django.contrib.auth import login
from .forms import CustomUserCreationForm



def index(request):
    context = {}
    return render(request, "myapp/index.html", context)

def login_page(request):
    return render(request, 'myapp/loginPage.html')

def rooms_page(request):
    return render(request, 'myapp/roomsPage.html')

def spa_page(request):
    return render(request, 'myapp/spaPage.html')

def golf_page(request):
    return render(request, 'myapp/golfPage.html')

def dining_page(request):
    return render(request, 'myapp/diningPage.html')

def seasonal_page(request):     
    return render(request, 'myapp/seasonalOffers.html')

def membership_page(request):   
    return render(request, 'myapp/membershipOffers.html')

def help_page(request):  
    return render(request, 'myapp/helpPage.html')

def bookings_page(request):
    return render(request, 'myapp/bookings.html')




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately after registration
            return redirect('myapp:index')  # Redirect to a home page or any page you like
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'myapp/customer_form.html', {'form': form})