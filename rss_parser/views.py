from django.shortcuts import render
from zak_parser.rss_parser import parser
from datetime import date, timedelta

# Create your views here.
def index(request):
    date_format = '%d.%m.%Y'
    yesterday = date.today() - timedelta(days=2)

    yesterday_f = str(yesterday.strftime(date_format))
    today_f = str(date.today().strftime(date_format))


    publ_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=onppRf615=on&fz94=on&&sortBy=UPDATE_DATE&af=on&updateDateFrom={yesterday_f}&updateDateTo={today_f}&priceFromGeneral=300000000&currencyIdGeneral=-1&customerPlaceWithNested=on&customerPlace=8408974%2C8408975&customerPlaceCodes=91000000000%2C92000000000'
    prot_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=onppRf615=on&fz94=on&&sortBy=UPDATE_DATE&pc=on&pa=on&updateDateFrom={yesterday_f}&updateDateTo={today_f}&priceFromGeneral=30000000&currencyIdGeneral=-1&customerPlaceWithNested=on&customerPlace=8408974%2C8408975&customerPlaceCodes=91000000000%2C92000000000'
    miac_publ_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=on&ppRf615=on&fz94=on&sortBy=UPDATE_DATE&af=on&updateDateFrom={yesterday_f}&updateDateTo={today_f}&currencyIdGeneral=-1&customerTitle=%D0%93%D0%9E%D0%A1%D0%A3%D0%94%D0%90%D0%A0%D0%A1%D0%A2%D0%92%D0%95%D0%9D%D0%9D%D0%9E%D0%95+%D0%91%D0%AE%D0%94%D0%96%D0%95%D0%A2%D0%9D%D0%9E%D0%95+%D0%A3%D0%A7%D0%A0%D0%95%D0%96%D0%94%D0%95%D0%9D%D0%98%D0%95+%D0%97%D0%94%D0%A0%D0%90%D0%92%D0%9E%D0%9E%D0%A5%D0%A0%D0%90%D0%9D%D0%95%D0%9D%D0%98%D0%AF+%D0%A1%D0%95%D0%92%D0%90%D0%A1%D0%A2%D0%9E%D0%9F%D0%9E%D0%9B%D0%AF+%22%D0%9C%D0%95%D0%94%D0%98%D0%A6%D0%98%D0%9D%D0%A1%D0%9A%D0%98%D0%99+%D0%98%D0%9D%D0%A4%D0%9E%D0%A0%D0%9C%D0%90%D0%A6%D0%98%D0%9E%D0%9D%D0%9D%D0%9E-%D0%90%D0%9D%D0%90%D0%9B%D0%98%D0%A2%D0%98%D0%A7%D0%95%D0%A1%D0%9A%D0%98%D0%99+%D0%A6%D0%95%D0%9D%D0%A2%D0%A0%22&customerCode=03742000172&customerFz94id=2128414&customerFz223id=365344&customerInn=9201014240'
    miac_prot_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=on&ppRf615=on&fz94=on&sortBy=UPDATE_DATE&pc=on&pa=on&updateDateFrom={yesterday_f}&updateDateTo={today_f}&currencyIdGeneral=-1&customerTitle=%D0%93%D0%9E%D0%A1%D0%A3%D0%94%D0%90%D0%A0%D0%A1%D0%A2%D0%92%D0%95%D0%9D%D0%9D%D0%9E%D0%95+%D0%91%D0%AE%D0%94%D0%96%D0%95%D0%A2%D0%9D%D0%9E%D0%95+%D0%A3%D0%A7%D0%A0%D0%95%D0%96%D0%94%D0%95%D0%9D%D0%98%D0%95+%D0%97%D0%94%D0%A0%D0%90%D0%92%D0%9E%D0%9E%D0%A5%D0%A0%D0%90%D0%9D%D0%95%D0%9D%D0%98%D0%AF+%D0%A1%D0%95%D0%92%D0%90%D0%A1%D0%A2%D0%9E%D0%9F%D0%9E%D0%9B%D0%AF+%22%D0%9C%D0%95%D0%94%D0%98%D0%A6%D0%98%D0%9D%D0%A1%D0%9A%D0%98%D0%99+%D0%98%D0%9D%D0%A4%D0%9E%D0%A0%D0%9C%D0%90%D0%A6%D0%98%D0%9E%D0%9D%D0%9D%D0%9E-%D0%90%D0%9D%D0%90%D0%9B%D0%98%D0%A2%D0%98%D0%A7%D0%95%D0%A1%D0%9A%D0%98%D0%99+%D0%A6%D0%95%D0%9D%D0%A2%D0%A0%22&customerCode=03742000172&customerFz94id=2128414&customerFz223id=365344&customerInn=9201014240'


    context = {'purc':parser(prot_url),
               'purch_nums':parser(prot_url).keys()}

    return render(request, 'rss_parser/index.html', context)