import time

import pytest
import self

from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest


class Test_Homepage(BaseTest):

    def test_get_homepage_title(self):
        self.homePage = HomePage(self.driver)
        title = self.homePage.get_HomePage_Title(TestData.HOME_TITLE)
        assert title == TestData.HOME_TITLE
        print(TestData.HOME_TITLE)

    def test_get_header_button(self):
        self.homePage = HomePage(self.driver)
        self.homePage.get_App_Gallery_Header_Btn()
        self.homePage.get_Google_Playstore_Header_Btn()
        self.homePage.get_App_Store_Header_Btn()

    def test_login_button_visible(self):
        self.homePage = HomePage(self.driver)
        flag = self.homePage.is_Login_Button_Exist
        assert flag

    def test_get_login_button_click(self):
        pytest.skip("Testcase skipped")

    def test_get_footer_button_is_exist(self):
        self.homePage = HomePage(self.driver)
        footer_bth = self.homePage.get_Footer_Btn

    def test_get_read_our_jour_text(self):
        self.homePage = HomePage(self.driver)
        text = self.homePage.get_Read_Our_Jour
        assert text == TestData.READ_OUT_JOUR_TEXT

    def test_get_dating_add(self):
        self.homePage = HomePage(self.driver)
        self.homePage.get_Dates_Add()
        self.homePage.get_Dating_Add()
        self.homePage.get_How_To_Add()



