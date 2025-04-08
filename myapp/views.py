from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, BookingForm
from .models import Booking



def index(request):
    context = {}
    return render(request, "myapp/index.html", context)


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


def login_page(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Authenticate the user
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('myapp:index')  # Redirect to the home page after successful login
            else:
                # Invalid login, form errors will show up
                form.add_error(None, "Invalid username or password")
    else:
        form = AuthenticationForm()

    return render(request, 'myapp/loginPage.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('myapp:index')  # Redirect to homepage after logout



@login_required
def bookings_page(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.save()
            return redirect('myapp:bookings')  # Refresh page or redirect as needed
    else:
        form = BookingForm()

    bookings = Booking.objects.filter(customer=request.user)

    return render(request, 'myapp/bookings.html', {
        'form': form,
        'bookings': bookings,
    })


@login_required
def update_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('myapp:bookings')
    else:
        form = BookingForm(instance=booking)

    return render(request, 'myapp/update_booking.html', {'form': form, 'booking': booking})


def delete_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    
    if request.method == 'POST':
        booking.delete()
        return redirect('myapp:bookings')  # assuming your bookings page URL name is 'bookings'
    
    return render(request, 'myapp/delete_booking.html', {'booking': booking})


@login_required
def all_bookings(request):
    if not request.user.is_staff:
        # If the user is not staff, redirect them to a different page (e.g., the home page or an error page)
        return redirect('myapp:home')  # Replace with your home URL or a custom error page
    bookings = Booking.objects.all()
    return render(request, 'myapp/all_bookings.html', {'bookings': bookings})