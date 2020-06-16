from django.shortcuts import render

# Create your views here.


def chat_room_view(request,*args,**kwargs):
    chat_room_name=kwargs['chat_room_name']

    return render(request,'chat_room.html',{'chat_room':chat_room_name})