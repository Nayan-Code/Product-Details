from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import Product

class InventoryConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, content):
        product_id = content['product_id']
        new_inventory = content['inventory_count']

        # Update inventory asynchronously
        product = await Product.objects.get(id=product_id)
        product.inventory_count = new_inventory
        await product.save()

        await self.send_json({
            'status': 'inventory updated',
            'product_id': product_id,
            'new_inventory': new_inventory,
        })
