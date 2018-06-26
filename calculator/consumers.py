from channels.generic.websocket import AsyncWebsocketConsumer
from .operations import calculate_index


class PricesConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    # Receive message from WebSocket
    async def receive(self, text_data):
        calculate_index(text_data)
