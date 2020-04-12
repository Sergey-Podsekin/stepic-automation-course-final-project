from .base_page import BasePage
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not " \
                                                                                   "presented "

    def should_be_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_COLOR), "Price is not presented"

    def same_price_in_title_and_product_tab(self):
        price1 = self.browser.find_element(*ProductPageLocators.PRICE_COLOR).text
        price2 = self.browser.find_element(*ProductPageLocators.PRICE_IN_PRODUCT_INFORMATION).text
        assert price1 == price2, f"Prices are not the same {price1} != {price2}"

    def same_titles_in_breadcrumb_and_main(self):
        title_breadcrumb = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_IN_BREADCRUMB).text
        title_main = self.browser.find_element(*ProductPageLocators.BOOK_TITLE_MAIN).text
        assert title_breadcrumb == title_main, f"Titles are not the same {title_breadcrumb} != {title_main}"

    def foo(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        BasePage.solve_quiz_and_get_code(self)
        time.sleep(1000)

    def should_be_message_added_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        BasePage.solve_quiz_and_get_code(self)
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BOOK_HAS_BEEN_ADDED), "No Added to basket message"

    def book_price_should_be_added_to_basket(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()
        BasePage.solve_quiz_and_get_code(self)
        price_main = self.browser.find_element(*ProductPageLocators.PRICE_COLOR).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        print(price_basket)
        print(price_main)
        assert price_main == price_basket, f"Prices are not the same: {price_main} != {price_basket}"
