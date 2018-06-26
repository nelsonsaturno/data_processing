from .models import SecurityPrice, SyntheticIndex
from datetime import timedelta, datetime


def return_of_security(last, prev):
    return (last.price / prev.price - 1) * last.security.weight


def calculate_index(timestamp):
    now = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
    last_prices = SecurityPrice.objects.filter(registered=now).order_by('security')
    prev_prices = SecurityPrice.objects.filter(
        registered__contains=now.date() - timedelta(days=1)
    ).order_by('security', '-registered').distinct('security')
    try:
        returns_securities = map(
            lambda prices: return_of_security(prices[0], prices[1]),
            zip(last_prices, prev_prices)
        )
    except IndexError:
        raise("There is an inconsistence with the security prices.")
    try:
        prev_index = SyntheticIndex.objects.filter(
            calculated__contains=now.date() - timedelta(days=1)
        ).order_by('-calculated')[0]
    except IndexError:
        raise("The Synthetic Index wasn't calculated yesterday.")
    new_index = SyntheticIndex(
        calculated=now, price=(sum(returns_securities) + 1) * prev_index.price
    )
    new_index.save()
