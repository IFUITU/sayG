from django.urls import re_path
from main.consumers import MessageConsumer

websocket_urlpatterns = [
    re_path("ws/chat/(?P<username>\w+)/$", MessageConsumer.as_asgi(), name="messanger"),

]