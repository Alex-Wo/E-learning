import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope['user']
        self.id = self.scope['url_route']['kwargs']['course_id']
        self.room_group_name = f'chat_{self.id}'
        # Присоединяемся к группе чата
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        # Принимаем соединение
        await self.accept()

    async def disconnect(self, close_code):
        # Покидаем группу чата
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Получаем сообщение из WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        now = timezone.now()
        # Отправляем сообщение в чат
        await self.channel_layer.group_send(self.room_group_name,
                                            {'type': 'chat_message', 'message': message,
                                             'user': self.user.username, 'datetime': now.isoformat()})

    # Получаем сообщение из группы чата
    async def chat_message(self, event):
        # Отправляем сообщение в WebSocket
        await self.send(text_data=json.dumps(event))
