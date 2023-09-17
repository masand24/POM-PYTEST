from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import allure
import pytest


class Test:

    @allure.severity(allure.severity_level.CRITICAL)
    def test_logo(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://pure.app//")
        status = self.driver.find_element(By.XPATH, "//a[@data-test-id='header-logo']").is_displayed()

        if status:
            assert True
        else:
            assert False

        self.driver.quit()

    @allure.severity(allure.severity_level.NORMAL)
    def test_setting(self):
        pytest.skip('Skipping test.. will implement it later')

    @allure.severity(allure.severity_level.BLOCKER)
    def test_login(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("https://pure.app//")
        self.driver.find_element(By.XPATH, "(//span[@id='app-button'])[1]").click()
        login = self.driver.find_element(By.XPATH, "(//button[@id='auth-modal-button-google']").is_displayed()

        if login:
            assert True
        else:
            assert False
        allure.attach(self.driver.get_screenshot_as_png(), name="Testloginscreen", attachment_type=AttachmentType.PNG)
        self.driver.quit()
