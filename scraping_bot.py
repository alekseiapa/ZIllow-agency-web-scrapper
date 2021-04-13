from bs4 import BeautifulSoup
import requests
import math
ELEMENTS_PER_PAGE = 41


class Scraper:

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36",
            "Accept-Language": "ru,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "Accept-Encoding": "gzip, deflate",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        }
        self.num_results = 0
        self.num_pages = 0
        self.content = None
        self.num_entries = 0
        self.cards_dict_list = []
        self.get_info(1)

    def get_info(self, num_page):
        r = requests.get(url=f"{self.base_url}{num_page}%7D%7D", headers=self.headers)
        soup = BeautifulSoup(r.content, 'html.parser')
        self.content = soup
        num_results = int(soup.find(class_="result-count").text.split()[0])
        num_pages = math.floor(num_results / ELEMENTS_PER_PAGE)
        self.num_results = num_results
        self.num_pages = num_pages
        self.get_content()
        print("Page finished... Moving to the next page...")


    def get_content(self):
        content = self.content
        cards = content.find_all("div", class_="list-card-info")
        for card in cards:
            # Append price
            card_price = card.find("div", class_="list-card-price")
            if "+" in card_price.text:
                price_text_normal = card_price.text.split("+")[0]
            elif "/" in card_price.text:
                price_text_normal = card_price.text.split("/")[0]
            else:
                price_text_normal = card_price.text.split()[0]

            # Append link
            card_link = card.find("a", href=True)['href']
            if card_link[0] == "/":
                card_link = f"https://www.zillow.com{card_link}"

            # Append address
            card_address = card.find("address", class_="list-card-addr")
            card_address_text = card_address.text

            # Create single card dictionary
            card_info = {
                    "Address": card_address_text,
                    "Price": price_text_normal,
                    "Link": card_link
                }
            self.num_entries += 1
            self.cards_dict_list.append(card_info)





