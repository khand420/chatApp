from django.urls import path
from django.urls import re_path
# from django.conf.urls import url 
from . import consumers
from . import group_consumers


websocket_urlpatterns = [
    # re_path(r'ws/chat/', consumers.SyncChatConsumer.as_asgi()),
    # re_path(r'ws/chat/', consumers.ChatConsumer.as_asgi()),
    path('ws/sc/chat/', consumers.SyncChatConsumer.as_asgi()),
    path('ws/ac/chat/', consumers.AsyncChatConsumer.as_asgi()),
    
 
    # re_path(r'ws/sc/chat/(?P<group>\w+)/$', group_consumers.SyncChatConsumer.as_asgi()),
    # re_path(r'ws/ac/chat/(?P<group>\w+)/$', group_consumers.AsyncChatConsumer.as_asgi()),

    path('ws/sc/chat/group/<str:group>/', group_consumers.SyncChatConsumer.as_asgi()),
    path('ws/ac/chat/group/<str:group>/', group_consumers.AsyncChatConsumer.as_asgi()),
    
    
    
    # re_path(r'ws/chat/$', consumers.SyncChatConsumer.as_asgi()),
    # url(r'ws/chat/', consumers.SyncChatConsumer.as_asgi()), 
]