from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy

from .models import Room, Category, Review, Restaurant
from .forms import ContactForm, ReviewForm, RoomForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import FormView, TemplateView


def home(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render(request, "hotels/home.html", context)


def accommodation(request):
    q = request.GET.get("q") if request.GET.get("q") is not None else ""
    rooms = Room.objects.filter(
        Q(category__name__icontains=q)
        | Q(room_number__icontains=q)
        | Q(size__icontains=q)
    )
    categories = Category.objects.all()
    room_count = rooms.count()
    context = {"rooms": rooms, "categories": categories, "room_count": room_count}
    return render(request, "hotels/accommodation.html", context)


def room_details(request, pk):
    room = Room.objects.get(id=pk)
    reviews = Review.objects.filter(approved=True).filter(room=room).all()
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                room=room,
                rating=form.cleaned_data["rating"],
                comment=form.cleaned_data["comment"],
            )
            review.save()
            return redirect("accommodation")
    context = {"room": room, "reviews": reviews, "form": form}
    return render(request, "hotels/room_details.html", context)


def restaurant(request):
    restaurants = Restaurant.objects.all()
    context = {"restaurants": restaurants}
    return render(request, "hotels/restaurant_bar.html", context)


def create_room(request):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("accommodation")
    context = {"form": form}
    return render(request, "hotels/room_form.html", context)


def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("accommodation")
    context = {"form": form}
    return render(request, "hotels/room_form.html", context)


def delete_room(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    return render(request, "hotels/delete.html", {"obj": room})


class ContactView(FormView):
    template_name = "hotels/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        form.send_email()
        return super().form_valid(form)


class ContactSuccessView(TemplateView):
    template_name = "hotels/success.html"
