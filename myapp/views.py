from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from forex_python.converter import CurrencyRates,CurrencyCodes
from .models import Currency


def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()

    try:
        converted_amount = c.convert(from_currency, to_currency, amount)
        return converted_amount
    except Exception as e:
        return str(e)

def index(request):
    currencies = Currency.objects.all()
    c1 = CurrencyCodes()
    if request.method == 'POST' and request.POST.get('amount'):
        
        amt = float(request.POST.get('amount'))
        f1 = str(request.POST.get('fromcurrency'))
        t1 = request.POST.get('tocurrency')
        s = convert_currency(amt,f1,t1)
        s = round(s,2)
        symbol = c1.get_symbol(t1)
        ans = f'{amt} {f1} to {t1} is {symbol} {s}'
        # messages.info(request,f'{f1} : {t1} : {amt} :\n {request.POST}')
        return render(request,'index.html',{'ans':ans,'currencies': currencies})

    return render(request,'index.html',{'currencies': currencies})

# currency_data = [
#     {"name": "US Dollar", "code": "USD"},
#     {"name": "Euro", "code": "EUR"},
#     {"name": "British Pound", "code": "GBP"},
#     {"name": "Japanese Yen", "code": "JPY"},
#     {"name": "Canadian Dollar", "code": "CAD"},
#     {"name": "Australian Dollar", "code": "AUD"},
#     {"name": "Swiss Franc", "code": "CHF"},
#     {"name": "Chinese Yuan", "code": "CNY"},
#     {"name": "Indian Rupee", "code": "INR"},
#     {"name": "Brazilian Real", "code": "BRL"},
#     {"name": "South African Rand", "code": "ZAR"},
#     {"name": "Mexican Peso", "code": "MXN"},
#     {"name": "Singapore Dollar", "code": "SGD"},
#     {"name": "Hong Kong Dollar", "code": "HKD"},
#     {"name": "Swedish Krona", "code": "SEK"},
#     {"name": "Norwegian Krone", "code": "NOK"},
#     {"name": "Danish Krone", "code": "DKK"},
#     {"name": "New Zealand Dollar", "code": "NZD"},
#     {"name": "Russian Ruble", "code": "RUB"},
#     {"name": "South Korean Won", "code": "KRW"},
# ]
# for data in currency_data:
#     currency = Currency(name=data["name"], code=data["code"])
#     currency.save()
#     print(f"Added {currency.name} ({currency.code}) to the database.")
