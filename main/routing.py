from django.urls import path
from .consumers import MessageConsumer

websocket_urlpatterns = [
    # re_path("ws//", MessageConsumer.as_asgi())
    # path("ws/(?P<room_name>\w+)/", MessageConsumer.as_asgi())
    path("ws/<int:pk>/", MessageConsumer.as_asgi())
]