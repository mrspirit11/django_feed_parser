from bs4 import BeautifulSoup as bs
import requests
import feedparser


UserAgent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 YaBrowser/20.4.2.150 (beta) Yowser/2.5 Safari/537.36'}
date_format = '%d.%m.%Y'
yesterday = date.today() - timedelta(days=1)

yesterday_f = str(yesterday.strftime(date_format))
today_f = str(date.today().strftime(date_format))

publ_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=onppRf615=on&fz94=on&&sortBy=UPDATE_DATE&af=on&updateDateFrom={yesterday_f}&updateDateTo={today_f}&priceFromGeneral=300000000&currencyIdGeneral=-1&customerPlaceWithNested=on&customerPlace=8408974%2C8408975&customerPlaceCodes=91000000000%2C92000000000'
prot_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=onppRf615=on&fz94=on&&sortBy=UPDATE_DATE&pc=on&pa=on&updateDateFrom={yesterday_f}&updateDateTo={today_f}&priceFromGeneral=30000000&currencyIdGeneral=-1&customerPlaceWithNested=on&customerPlace=8408974%2C8408975&customerPlaceCodes=91000000000%2C92000000000'
miac_publ_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=on&ppRf615=on&fz94=on&sortBy=UPDATE_DATE&af=on&updateDateFrom={yesterday_f}&updateDateTo={today_f}&currencyIdGeneral=-1&customerTitle=%D0%93%D0%9E%D0%A1%D0%A3%D0%94%D0%90%D0%A0%D0%A1%D0%A2%D0%92%D0%95%D0%9D%D0%9D%D0%9E%D0%95+%D0%91%D0%AE%D0%94%D0%96%D0%95%D0%A2%D0%9D%D0%9E%D0%95+%D0%A3%D0%A7%D0%A0%D0%95%D0%96%D0%94%D0%95%D0%9D%D0%98%D0%95+%D0%97%D0%94%D0%A0%D0%90%D0%92%D0%9E%D0%9E%D0%A5%D0%A0%D0%90%D0%9D%D0%95%D0%9D%D0%98%D0%AF+%D0%A1%D0%95%D0%92%D0%90%D0%A1%D0%A2%D0%9E%D0%9F%D0%9E%D0%9B%D0%AF+%22%D0%9C%D0%95%D0%94%D0%98%D0%A6%D0%98%D0%9D%D0%A1%D0%9A%D0%98%D0%99+%D0%98%D0%9D%D0%A4%D0%9E%D0%A0%D0%9C%D0%90%D0%A6%D0%98%D0%9E%D0%9D%D0%9D%D0%9E-%D0%90%D0%9D%D0%90%D0%9B%D0%98%D0%A2%D0%98%D0%A7%D0%95%D0%A1%D0%9A%D0%98%D0%99+%D0%A6%D0%95%D0%9D%D0%A2%D0%A0%22&customerCode=03742000172&customerFz94id=2128414&customerFz223id=365344&customerInn=9201014240'
miac_prot_url = f'https://zakupki.gov.ru/epz/order/extendedsearch/rss.html?morphology=on&search-filter=%D0%94%D0%B0%D1%82%D0%B5+%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%89%D0%B5%D0%BD%D0%B8%D1%8F&pageNumber=1&sortDirection=false&recordsPerPage=_10&showLotsInfoHidden=false&fz44=on&fz223=on&ppRf615=on&fz94=on&sortBy=UPDATE_DATE&pc=on&pa=on&updateDateFrom={yesterday_f}&updateDateTo={today_f}&currencyIdGeneral=-1&customerTitle=%D0%93%D0%9E%D0%A1%D0%A3%D0%94%D0%90%D0%A0%D0%A1%D0%A2%D0%92%D0%95%D0%9D%D0%9D%D0%9E%D0%95+%D0%91%D0%AE%D0%94%D0%96%D0%95%D0%A2%D0%9D%D0%9E%D0%95+%D0%A3%D0%A7%D0%A0%D0%95%D0%96%D0%94%D0%95%D0%9D%D0%98%D0%95+%D0%97%D0%94%D0%A0%D0%90%D0%92%D0%9E%D0%9E%D0%A5%D0%A0%D0%90%D0%9D%D0%95%D0%9D%D0%98%D0%AF+%D0%A1%D0%95%D0%92%D0%90%D0%A1%D0%A2%D0%9E%D0%9F%D0%9E%D0%9B%D0%AF+%22%D0%9C%D0%95%D0%94%D0%98%D0%A6%D0%98%D0%9D%D0%A1%D0%9A%D0%98%D0%99+%D0%98%D0%9D%D0%A4%D0%9E%D0%A0%D0%9C%D0%90%D0%A6%D0%98%D0%9E%D0%9D%D0%9D%D0%9E-%D0%90%D0%9D%D0%90%D0%9B%D0%98%D0%A2%D0%98%D0%A7%D0%95%D0%A1%D0%9A%D0%98%D0%99+%D0%A6%D0%95%D0%9D%D0%A2%D0%A0%22&customerCode=03742000172&customerFz94id=2128414&customerFz223id=365344&customerInn=9201014240'

urls=[publ_url,prot_url,miac_publ_url,miac_prot_url]

def parse_sites(url_):

    def get_rss_zakupki():
        """Получаем ссылку на rss zakupki.gov Bи возвращаем список №"""
        feed = feedparser.parse(url_)
        purchase_links = [ent['link'] for ent in feed['entries']]
        purchase_numbers = [link.split('=')[1] for link in purchase_links]
        updated = []
        links = []
        for feed in feed['entries']:
            summary_html = feed['summary']
            summary_soup = bs(summary_html, 'html.parser')
            upd = summary_soup.text[summary_soup.text.find('Обновлено:'):].split('Этап')[
                0]
            updated.append(upd)
            links.append(feed['link'])
        return list(zip(updated, purchase_numbers, links))

    def parse_kontur(list_of_purch_nums):
        k_url = 'https://zakupki.kontur.ru/'
        out = []
        for upd, num, link in list_of_purch_nums:
            if len(num) < 16:
                continue
            page = requests.get(
                k_url + num, headers=UserAgent)
            soup = bs(page.text, 'html.parser')
            # Название
            try:
                title = soup.select('h1')[0].text
            except Exception:
                continue
            status = soup.find('p', class_='tenderPurchaseStatus_name')
            # Блок цен
            price_block = soup.find(
                'div', attrs={'class': 'priceWrap priceWrap__main'})
            price_titles = price_block.findAll(
                'dt', attrs={'class': 'tenderField_title'})
            price_title = ['<tr><td>' + title.text +
                           '</td>' for title in price_titles]
            price_values = price_block.findAll(
                'span', attrs={'class': 'tenderPrice'})
            price_value = [
                '<td><b>' + value.text.split('  ')[0] + '</b></td></tr>' for value in price_values]
            price_with_value = ''.join(
                [i + j for i, j in zip(price_title, price_value)])
            # Блок Порядок размещения
            content_block = soup.find('div', attrs={'class': 'tender_rules'})
            content_type = content_block.find('p').text
            content_dates = content_block.findAll(
                'dl', attrs={'class': 'clearfix tenderField tenderField__m'})
            content_date = [date.text.strip() for date in content_dates]
            # Блок Заказчик
            try:
                customer_block = soup.find('div', attrs={'class': 'tender_customer'})
                customer_name = customer_block.find(
                    'div', {'class': 'tender_customer_name'}).text.strip()
                customer_INN = customer_block.find('p').text.strip()
            except Exception:
                customer_name = ''
            # Вывод
            n_out = {'num': num, 'title': title,
                     'content_type': content_type,
                     'content_date': content_date,
                     'upd': upd, 'price': price_with_value,
                     'status': status, 'link': link,
                     'customer_name': customer_name}
            out.append(n_out)
        return out

    def parse_zakupki(list_of_purch_nums):
        out = {}
        for upd, num, link in list_of_purch_nums:
            if len(num) < 16:
                continue
            print(num)
            url = 'https://zakupki.gov.ru/epz/order' + \
                  '/notice/ea44/view/supplier-results.html?regNumber=' + num
            page = requests.get(url, headers=UserAgent)
            soup = bs(page.text, 'html.parser')
            result_table = soup.find('article')
            if result_table.find('i') :
                continue
            td = [t.text for t in result_table.findAll('td', class_='tableBlock__col')[2:]]
            # td = [tr_.findAll('td') for tr_ in tr]
            # print(td)
            if len(td)>2:
                html_out = '<table>\
                            <tr><td>{}</td></tr><tr><td>{}</td></tr>\
                            <tr><td>{}</td></tr><tr><td>{}</td></tr>\
                            </table>'.format(td[0], td[1], td[2], td[3] if len(td)>3 else '')
            else:
                html_out = '<table>\
                            <tr><td>{}</td></tr>\
                            </table>'.format(td[0])
            out_ = {num: html_out}
            out.update(out_)
        return out
    list_of_purch = get_rss_zakupki()
    return parse_kontur(list_of_purch), parse_zakupki(list_of_purch)


def main(urls):
    for url in urls:
        parse_sites(url)

if __name__ == '__main__':
    main(urls)
