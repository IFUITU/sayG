from django.urls import path
from .views import lobby, room, rooms, RoomApiView, MessageApiView, RoomDetailView

app_name="main"
urlpatterns = [
    path("lobby/<int:pk>/", lobby, name="lobby"),
    path("rooms/", rooms, name="rooms"),
    path("rooms/<str:slug>/", room, name="room"),

    path("room/<int:pk>/", RoomDetailView.as_view(), name="room-detail"),
    path("room/", RoomApiView.as_view(), name="room_list"),
]