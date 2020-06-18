from django.shortcuts import render
from django.http import Http404
# Create your views here.


def chat_room_view(request,*args,**kwargs):
    chat_room_name=kwargs['chat_room_name']
    print('printing in view',kwargs)
    temp=request.scope['path'].split('?')[1].split('&&')
    for i in temp:
        if 'username' in i.split('=')[0]:
            return render(request,'chat_room.html',{'chat_room':chat_room_name,'name':i.split('=')[1]})


    

    raise Http404