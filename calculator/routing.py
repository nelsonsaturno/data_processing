from django.conf.urls import url
from consumers import PricesConsumer


websocket_urlpatterns = [
    url(r'^ws/prices/$', PricesConsumer),
]
