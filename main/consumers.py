import json
from asgiref.sync import async_to_sync, sync_to_async

from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async

from .models import Message

class MessageConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        
        self.room_name = self.scope['url_route']['kwargs']
        self.room_group_name = 'chat_%s' % "helllo"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(self.scope['user'], self.room_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_json = json.dumps(text_data)
        print(text_data, "asdjhashdasjd")
        # message = text_json['message']
    
        # self.send(text_data=json.dumps({
        #     'type':"chat",
        #     "message":message,
        # }))

        # await self.channel_layer.group_send(
        #     self.room_group_name,
        #     {
        #         "type":'chat_message',
        #         "message":message
        #     }
        # )

    async def chat_message(self, event):
        message = event['message']
        data={"message":message}
        # new_msg =  async_to_sync(self.create_chat(data))
        # print(new_msg.text)
        self.send(text_data=json.dumps({
            "type":'chat',
            'message':message,
        }))

 

# class MessageConsumer(WebsocketConsumer):
#     @database_sync_to_async
#     def create_chat(self, data):
#         obj = Message.objects.create(user=self.scope['user'], text=data['message'])
#         return obj
         
#     def connect(self):
#         self.accept()
#         print(self.scope['user'])
#         # self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_name = "room_test_name" #self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = 'chat_{}'.format(self.scope['user'])
        
#         print(self.scope['url_route'])
#         async_to_sync(self.channel_layer.group_add)(
#             self.room_group_name,
#             self.channel_name
#         )

#         self.send(text_data=json.dumps({
#             "type":"Connection Established",
#             "msg":"Hello Connected"
#         }))

#     def disconnect(self, close_code):
#         async_to_sync(self.channel_layer.group_discard)(
#             self.room_group_name,
#             self.channel_name
#         )
    
#     def receive(self, text_data):
#         text_json = json.loads(text_data)
#         message = text_json['message']
#         print(message)
#         self.send(text_data=json.dumps({
#             'type':"chat",
#             "message":message,
#         }))

#         async_to_sync(self.channel_layer.group_send)(
#             self.room_group_name,
#             {
#                 "type":'chat_message',
#                 "message":message
#             }
#         )

#     def chat_message(self, event):
#         message = event['message']
#         data={"message":message}
#         new_msg =  async_to_sync(self.create_chat(data))
#         print(new_msg.text)
#         self.send(text_data=json.dumps({
#             "type":'chat',
#             'message':message,
#         }))

 

