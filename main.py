from scraping_bot import Scraper
from google_bot import GoogleFormBot

BASE_URL = "BASE_URL"
WEBSITE_URL ="WEBSITE_URL"
BASE_URL_FORM = "BASE_URL_FORM"


website_scraper = Scraper(WEBSITE_URL)
google_form_bot = GoogleFormBot()
google_form_bot.login(BASE_URL_FORM)

for i in range(2, 5):
    website_scraper.get_info(i)

for card in website_scraper.cards_dict_list:
    google_form_bot.fill_the_data(card["Address"], card["Price"], card["Link"])
