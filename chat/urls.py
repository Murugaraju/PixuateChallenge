from django.urls import path
from django.views.generic import TemplateView
from .views import chat_room_view
urlpatterns = [
    path('',TemplateView.as_view(template_name='index.html')),
    path('<str:chat_room_name>',chat_room_view)
]