from channels.generic.websocket import AsyncWebsocketConsumer
from django.db import connection
from django.db.utils import OperationalError
from channels.db import database_sync_to_async
from django.core import serializers
from django.utils import timezone
import json
from .models import *
from urllib.parse import urlparse
import datetime
import time

class ChatConsumer(AsyncWebsocketConsumer):
    groups = ['broadcast']

    async def connect(self):
        try:
            await self.accept()
            self.room_group_name = self.scope['url_route']['kwargs']['room_name']
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
        except Exception as e:
            raise

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        await self.close()

    async def receive(self, text_data):
        try:
            print(str(text_data))
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            name = text_data_json['name']
            await self.createMessage(text_data_json)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'name': name,
                }
            )
        except Exception as e:
            raise

    async def chat_message(self, event):
        try:
            message = event['message']
            name = event['name']
            await self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': message,
                'name': name,
            }))
        except Exception as e:
            raise

    @database_sync_to_async
    def createMessage(self, event):
        try:
            room = Room.objects.get(
                name=self.room_group_name
            )
            Message.objects.create(
                room=room,
                name=event['name'],
                content=event['message']
            )
        except Exception as e:
            raise
