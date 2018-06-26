from channels.generic.websocket import AsyncWebsocketConsumer
from .operations import calculate_index


class PricesConsumer(AsyncWebsocketConsumer):
    """
    Create a Websocket consumer
    """

    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        """
        Once the message is received, calculate the new index price
        """
        calculate_index(text_data)
