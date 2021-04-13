from selenium import webdriver
import time
CHROME_DRIVER_PATH = "chromedriver"

class GoogleFormBot:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)

    def login(self, url):
        driver = self.driver
        driver.get(url)
        time.sleep(2)

    def fill_the_data(self, address, price, link):
        driver = self.driver
        fields = driver.find_elements_by_class_name("exportInput")
        fields[0].send_keys(address)
        fields[1].send_keys(price)
        fields[2].send_keys(link)
        submit_button = driver.find_element_by_xpath("/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div/div")
        submit_button.click()
        time.sleep(3)
        submit_one_more = driver.find_element_by_link_text("Submit another response")
        submit_one_more.click()
        time.sleep(3)
        print("Data is filled... Moving to next form...")
