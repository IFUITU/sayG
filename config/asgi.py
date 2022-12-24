# import os

# import django
# from channels.http import AsgiHandler
# from channels.routing import ProtocolTypeRouter,get_default_application


# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()


# application=get_default_application()


import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from main.routing import websocket_urlpatterns

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# django.setup()


application = ProtocolTypeRouter({
   "http":get_asgi_application(),
   "websocket":AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
   )

})