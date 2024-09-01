from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from concert.forms import LoginForm, SignUpForm
from concert.models import Concert, ConcertAttending

import requests as req

# Signup view
def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).first()
        if user:
            return render(request, "signup.html", {"form": SignUpForm(), "message": "User already exists"})
        else:
            user = User.objects.create(username=username, password=make_password(password))
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
    return render(request, "signup.html", {"form": SignUpForm()})

# Index view
def index(request):
    return render(request, "index.html")

# Songs view
def songs(request):
    songs_url = os.getenv('SONGS_URL', 'http://default_songs_url/song')
    try:
        response = req.get(songs_url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        songs = response.json()
        return render(request, "songs.html", {"songs": songs.get("songs", [])})
    except req.RequestException as e:
        # Handle request exceptions
        return render(request, "songs.html", {"error": str(e)})

# Photos view
def photos(request):
    photos_url = os.getenv('PHOTO_URL', 'http://default_photos_url/picture')
    try:
        response = req.get(photos_url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        photos = response.json()
        return render(request, "photos.html", {"photos": photos})
    except req.RequestException as e:
        # Handle request exceptions
        return render(request, "photos.html", {"error": str(e)})

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
        except User.DoesNotExist:
            return render(request, "login.html", {"form": LoginForm})
    return render(request, "login.html", {"form": LoginForm})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
# Concerts view
def concerts(request):
    concerts = Concert.objects.all()
    return render(request, "concerts.html", {"concerts": concerts})

# Concert detail view
def concert_detail(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(Concert, pk=id)
        try:
            status = obj.attendee.filter(user=request.user).first().attending
        except:
            status = "-"
        return render(request, "concert_detail.html", {"concert_details": obj, "status": status, "attending_choices": ConcertAttending.AttendingChoices.choices})
    else:
        return HttpResponseRedirect(reverse("login"))

# Concert attendee view
def concert_attendee(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            concert_id = request.POST.get("concert_id")
            attendee_status = request.POST.get("attendee_choice")
            concert_attendee_object = ConcertAttending.objects.filter(
                concert_id=concert_id, user=request.user).first()
            if concert_attendee_object:
                concert_attendee_object.attending = attendee_status
                concert_attendee_object.save()
            else:
                ConcertAttending.objects.create(concert_id=concert_id,
                                                user=request.user,
                                                attending=attendee_status)
        return HttpResponseRedirect(reverse("concerts"))
    else:
        return HttpResponseRedirect(reverse("index"))
