from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import SyntheticIndex


class GetIndexPrices(APIView):
    """
    API service to get all the index prices by date
    """
    renderer_classes = (JSONRenderer, )

    def get(self, request, format=None):
        index_prices = SyntheticIndex.objects.all().order_by("-calculated")
        content = {}
        for price in index_prices:
            try:
                if content[str(price.calculated.date())]:
                    continue
            except KeyError:
                content[str(price.calculated.date())] = price.price
        return Response(content)
