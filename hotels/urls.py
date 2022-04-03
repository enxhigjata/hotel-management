from django.urls import path
from . import views

urlpatterns = [
    path("room_list/", views.room_list, name="room_list"),
    path("room_details/<int:pk>/", views.room_details, name="room_details"),
    path("create-room/", views.create_room, name="create-room"),
    path("update-room/<int:pk>/", views.update_room, name="update-room"),
    path("delete-room/<int:pk>/", views.delete_room, name="delete-room"),
]
