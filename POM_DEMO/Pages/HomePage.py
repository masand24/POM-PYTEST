import allure
from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.BasePage import BasePage


@allure.severity(allure.severity_level.CRITICAL)
class HomePage(BasePage):
    HEADER_TEXT = (By.XPATH, "//a[@data-test-id='header-logo']")
    LOGIN_BUTTON = (By.XPATH, "//span[@id='app-button']")
    HEADER_APP_STORE_BTN = (By.XPATH, "//a[@data-test-id='app_store_first_section']")
    HEADER_GOOGLE_PLAYSTORE_BTN = (By.XPATH, "//a[@data-test-id='google_play_first_section']")
    HEADER_APP_GALLERY_BTN = (By.XPATH, "//a[@data-test-id='app_gallery_first_section']")
    HEADER_HAMBURG_BTN = (By.XPATH, "//a[@data-test-id='header-hamburger-btn']")
    DATES_AD = (By.XPATH, "//a[@data-test-id='articles-pure-ads']")
    HOW_TO_AD = (By.XPATH, "//a[@data-test-id='articles-more-matches-on-Pure']")
    DATING_AD = (By.XPATH, "//a[@data-test-id='articles-dating-and-self-discovery']")
    READ_OUR_JOUR = (By.XPATH, "//a[@data-test-id='articles-to-journal']")
    FOOTER_APP_STORE_BTN = (By.XPATH, "//a[@data-test-id='app_store_footer']")
    FOOTER_GOOGLE_PLAYSTORE_BTN = (By.XPATH, "//a[@data-test-id='google_play_footer']")
    FOOTER_APP_GALLERY_BTN = (By.XPATH, "//a[@data-test-id='app_gallery_footer']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.Base_Url)

    def get_HomePage_Title(self, title):
        return self.get_title(title)

    def is_Login_Button_Exist(self):
        return self.is_visible(self.LOGIN_BUTTON)

    def click_Login(self):
        self.do_click(self.LOGIN_BUTTON)

    def get_App_Store_Header_Btn(self):
        self.is_visible(self.HEADER_APP_STORE_BTN)

    def get_Google_Playstore_Header_Btn(self):
        self.is_visible(self.HEADER_GOOGLE_PLAYSTORE_BTN)

    def get_App_Gallery_Header_Btn(self):
        self.is_visible(self.HEADER_APP_STORE_BTN)

    def get_Dates_Add(self):
        self.is_visible(self.DATES_AD)

    def get_How_To_Add(self):
        self.is_visible(self.HOW_TO_AD)

    def get_Dating_Add(self):
        self.is_visible(self.DATING_AD)

    def get_Read_Our_Jour(self):
        self.get_element_text(self.READ_OUR_JOUR)

    def get_Footer_Btn(self):
        self.is_visible(self.FOOTER_APP_STORE_BTN)
        self.is_visible(self.FOOTER_GOOGLE_PLAYSTORE_BTN)
        self.is_visible(self.FOOTER_APP_GALLERY_BTN)
