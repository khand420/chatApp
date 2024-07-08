

from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync
import json



class AsyncChatConsumer(AsyncConsumer):   
    async def websocket_connect(self, event):
        print('WebSocket Connected....', event)
        print('Channel Layer....', self.channel_layer)
        print('Channel Name....', self.channel_name)
        
        #add Group into puspa
        my_group = self.group_name = self.scope['url_route']['kwargs']['group']
        print('Group Name....', my_group.group)
        await self.channel_layer.group_add(
            my_group,
            self.channel_name
            )
        
        await self.send({
            'type': 'websocket.accept'
        })

    async def websocket_receive(self, event):
        print('Message Received from client....', event)
        print('Message Received from client....', type(event['text']))
        
        # self.send({
        #     'type': 'websocket.send',
        #     'text': 'Message received' 
        # })
        
        my_group = self.group_name = self.scope['url_route']['kwargs']['group']
        await self.channel_layer.group_send(
            my_group,{
            'type': 'websocket.send',
            'message': event['text']
            })
        
    # handler use func name as type value
    async def websocket_send(self, event):
        print("Event....", event)
        print("Actual Data....", type(event['message']))
        await self.send({
            'type': 'websocket.send',
            'text': event['message']
            })
        
                       

    async def websocket_disconnect(self, event):
        print('WebSocket disconnected....', event)
        
        print('Channel Layer....', self.channel_layer)
        print('Channel Name....', self.channel_name)
        
        my_group = self.group_name = self.scope['url_route']['kwargs']['group']
        
        await self.channel_layer.group_discard(
            my_group,
            self.channel_name
            )
        raise StopConsumer() 



# This is for sync consumer 
class SyncChatConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print('WebSocket Connected....', event)
        print('Channel Layer....', self.channel_layer)
        print('Channel Name....', self.channel_name)
        
        #add Group into puspa
        my_group = self.group_name = self.scope['url_route']['kwargs']['group']
        
        async_to_sync(self.channel_layer.group_add)(
            my_group,
            self.channel_name
            )
        
        self.send({
            'type': 'websocket.accept'
        })

    def websocket_receive(self, event):
        print('Message Received from client....', event)
        print('Message Received from client....', type(event['text']))
        
        # self.send({
        #     'type': 'websocket.send',
        #     'text': 'Message received' 
        # })
        
        my_group = self.group_name = self.scope['url_route']['kwargs']['group']
        
        async_to_sync(self.channel_layer.group_send)(
            my_group,{
            'type': 'websocket.send',
            'message': event['text']
            })
        
    # handler use func name as type value
    def websocket_send(self, event):
        print("Event....", event)
        print("Actual Data....", type(event['message']))
        self.send({
            'type': 'websocket.send',
            'text': event['message']
            })
        
                       

    def websocket_disconnect(self, event):
        print('WebSocket disconnected....', event)
        
        print('Channel Layer....', self.channel_layer)
        print('Channel Name....', self.channel_name)
        my_group = self.group_name = self.scope['url_route']['kwargs']['group']
        
        async_to_sync(self.channel_layer.group_discard)(
            my_group,
            self.channel_name
            )
        raise StopConsumer() 






# from channels.generic.websocket import AsyncWebsocketConsumer
# import json

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         # await self.accept()
#         print('WebSocket Connected....')

#     async def receive(self, text_data):
#         print('Message Received from client....', text_data)
#         await self.send(text_data=json.dumps({
#             'message': 'Message received'
#         }))

#     async def disconnect(self, close_code):
#         print('WebSocket disconnected....', close_code)






    # def connect(self):
    #     self.room_name = 'chat'
    #     self.channel_group_name = 'chat_group'
        
    #     async_to_sync(self.channel_layer.group_add)(
    #         self.channel_group_name, self.room_name
    #         )
    #     self.accept()
    #     self.send(text_data = json.dumps({"status": 'connected'}))
    
    
    
    # # def receive(self, text_data):
    # #     print('Message Received from client....', text_data)
    # #     # await self.send(text_data=json.dumps({
    # #     #     'message': 'Message received'
    #     # }))
        
    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     # Broadcast the received message to all clients
    #     self.send(text_data=json.dumps({
    #         'type':'websocket.send',
    #         'message': message,     
    #     }))

    # def disconnect(self, close_code):
    #     print('WebSocket disconnected....', close_code)
    
    
    
    
    
    # def websocket_connect(self, event):
    #     self.send({
    #         'type': 'websocket.accept'
    #     })
    #     print('WebSocket Connected....', event)

    # def websocket_receive(self, event):
    #     print('Message Received from client....', event)
    #     self.send({
    #         'type': 'websocket.send',
    #         'text': 'Message received'
    #     })

    # def websocket_disconnect(self, event):
    #     print('WebSocket disconnected....', event)
    #     raise StopConsumer() 



