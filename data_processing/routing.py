from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import calculator.routing


# Routing the Websocket urls
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            calculator.routing.websocket_urlpatterns
        )
    ),
})
