from django.urls import path
from .views import lobby, room, rooms, RoomApiView, MessageApiView, RoomDetailView, MessageByRoom

app_name="main"
urlpatterns = [
    path("lobby/<int:pk>/", lobby, name="lobby"),
    path("rooms/", rooms, name="rooms"),
    path("rooms/<str:slug>/", room, name="room"),

    path("room/<int:pk>/", RoomDetailView.as_view(), name="room-detail"),
    path("room/", RoomApiView.as_view(), name="room_list"),

    path("messages-by-room/<int:room_id>/", MessageByRoom.as_view(), name="msg-by-room"),
    path("message/", MessageApiView.as_view(), name="msg")
]