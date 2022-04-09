from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accommodation/", views.accommodation, name="accommodation"),
    path("room_details/<int:pk>/", views.room_details, name="room_details"),
    path("restaurant_bar", views.restaurant, name="restaurant"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<int:pk>/", views.update_room, name="update-room"),
    path("delete-room/<int:pk>/", views.delete_room, name="delete-room"),
    path("contact/", views.contact, name="contact"),
]
