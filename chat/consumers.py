from channels.consumer import AsyncConsumer
# from asgiref.sync import async_to_sync
import json
# from channels.layers import get_channel_layer


class ChatChannel(AsyncConsumer):

  

    async def websocket_connect(self,event):
        # print('printing channel name--->',self.scope['query_string'].decode().split('=')[1])
        # print('printing channel layer--->',self.channel_layer)
        self.username=self.scope['query_string'].decode().split('=')[1]
        self.chat_room=self.scope['url_route']['kwargs']['chat_room']
        await self.send({
            'type':'websocket.accept'
        })
        await self.channel_layer.group_add(
            self.chat_room,
            self.channel_name)
        await self.send({
            'type':'websocket.send',
            'text':str(self.channel_name)
        })

    async def websocket_receive(self,event):

        print('message recieved',self,event)
        data=json.dumps({'message':event['text'],'channelName':self.channel_name,'username':self.username})
        await self.channel_layer.group_send(self.chat_room,{
            'type':'chat_message',
            'text':data
        })

    async def websocket_disconnect(self,event):
        #Todo client initiate discconect this will trigger
        print('Came')
        await self.channel_layer.group_discard(
            group=self.chat_room,
            channel=self.channel_name
        )

    async def chat_message(self,event):
        await self.send({
            'type':'websocket.send',
            'text':event['text']
        })