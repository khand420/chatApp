"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from app.routing import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(websocket_urlpatterns),  # Add your WebSocket URL routing here, for example: ('/ws', ChatConsumer)  # Replace ChatConsumer with your actual consumer class name.
        
})



# application = ProtocolTypeRouter({ 
#   "http": get_asgi_application(), 
#   "websocket": AuthMiddlewareStack( 
#         URLRouter( 
#             websocket_urlpatterns
#         ) 
#     ), 
# }) 
