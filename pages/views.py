from django.shortcuts import render

from hotels.models import Room


def home(request):
    rooms = Room.objects.all()
    return render(request, "pages/home.html", context={"rooms": rooms})
