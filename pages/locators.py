from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary")
    PRICE_COLOR = (By.CSS_SELECTOR, ".col-sm-6 .price_color")
    PRICE_IN_PRODUCT_INFORMATION = (By.CSS_SELECTOR, ".table tr:nth-child(3) td")
    BOOK_TITLE_IN_BREADCRUMB = (By.CSS_SELECTOR, ".breadcrumb .active")
    BOOK_TITLE_MAIN = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info strong")
    MESSAGE_BOOK_HAS_BEEN_ADDED = (By.CSS_SELECTOR, "#messages>.alert:nth-child(1) strong")