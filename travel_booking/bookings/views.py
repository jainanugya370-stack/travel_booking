from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import TravelOption, Booking
from django.utils import timezone

# Register user
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'bookings/register.html', {'form': form})

# Login user
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'bookings/login.html', {'error': 'Invalid credentials'})
    return render(request, 'bookings/login.html')

# Logout user
def logout_view(request):
    logout(request)
    return redirect('login')

from django.utils.dateparse import parse_date

@login_required
def home_view(request):
    travel_type = request.GET.get('type')
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    date_str = request.GET.get('date')

    options = TravelOption.objects.all()

    if travel_type:
        options = options.filter(travel_type__iexact=travel_type)
    if source:
        options = options.filter(source__icontains=source)
    if destination:
        options = options.filter(destination__icontains=destination)
    if date_str:
        try:
            date = parse_date(date_str)
            if date:
                options = options.filter(date_time__date=date)
        except:
            pass

    return render(request, 'bookings/home.html', {'options': options})



from .forms import BookingForm
from django.shortcuts import get_object_or_404
from django.contrib import messages

@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.status == 'Confirmed':
        booking.status = 'Cancelled'
        booking.travel_option.available_seats += booking.number_of_seats
        booking.travel_option.save()
        booking.save()

    return redirect('my_bookings')


@login_required
def book_travel(request):
    if request.method == 'POST':
        option_id = request.POST.get('travel_option_id')
        seats = int(request.POST.get('number_of_seats'))

        travel_option = get_object_or_404(TravelOption, id=option_id)

        if seats > travel_option.available_seats:
            messages.error(request, "Not enough seats available.")
            return redirect('home')

        total_price = travel_option.price * seats

        Booking.objects.create(
            user=request.user,
            travel_option=travel_option,
            number_of_seats=seats,
            total_price=total_price,
        )

        travel_option.available_seats -= seats
        travel_option.save()

        messages.success(request, "Booking successful!")
        return redirect('my_bookings')
