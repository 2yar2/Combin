from pages.product_page import ProductPage
from selenium import webdriver
import conftest


class TestUserWhatIsIncluded:
    def test_open_page(self, browser):
        
        product_page = ProductPage(browser, 'https://www.combin.com/product/instagram-growth/')
        product_page.open()
        product_page.cookies_close()
        product_page.click_to_growth()
        product_page.click_to_advanced()
        product_page.click_to_gender()
        product_page.click_to_machine()
        product_page.click_to_audience()
        product_page.click_to_repetitive()
        product_page.click_to_multiple()