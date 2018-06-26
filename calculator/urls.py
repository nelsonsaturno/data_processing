from django.urls import path
from . import api_views


urlpatterns = [
    path('get-index-prices/', api_views.GetIndexPrices.as_view(), name='get_index_prices'),
]
