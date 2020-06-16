from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chat.consumers import ChatChannel
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
    'websocket':URLRouter([
        path('ws/chat/<str:chat_room>',ChatChannel, name='chatsocket')
    ])
})