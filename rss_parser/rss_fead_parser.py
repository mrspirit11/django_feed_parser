import feedparser
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime, timedelta
from pprint import pprint as pp


update_from = (datetime.now() - timedelta(days=1)).strftime('%d.%m.%Y')
start_price = '30000000'

rss_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?\
morphology=on&pageNumber=1&sortDirection=false&recordsPerPage=_10&\
showLotsInfoHidden=false&sortBy=UPDATE_DATE&\
fz44=on&fz223=on&ppRf615=on&fz94=on&\
af=on&ca=on&pc=on&pa=on&selectedSubjectsIdNameHidden=%7B%7D&\
priceContractAdvantages44IdNameHidden=%7B%7D&\
priceContractAdvantages94IdNameHidden=%7B%7D&\
updateDateFrom={update_from}&priceFromGeneral={start_price}&\
currencyIdGeneral=-1&customerPlace=8408974%2C8408975&\
customerPlaceCodes=%2C&OrderPlacementSmallBusinessSubject=on&\
OrderPlacementRnpData=on&OrderPlacementExecutionRequirement=on&\
orderPlacement94_0=0&orderPlacement94_1=0&\
orderPlacement94_2=0&contractPriceCurrencyId=-1&\
budgetLevelIdNameHidden=%7B%7D&nonBudgetTypesIdNameHidden=%7B%7D'

feeds = feedparser.parse(rss_url)
pp(feeds['entries'][0])