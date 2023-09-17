import pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v116.page import capture_screenshot
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from PIL import Image
import allure
import os


@pytest.fixture(params=["chrome"], scope='class')
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = web_driver

    # Add a finalizer to handle screenshot capture and close the driver
    def teardown():
        if request.node.failed:
            # Capture a screenshot if the test case fails
            capture_screenshot(request.node.name)
        web_driver.close()

    request.addfinalizer(teardown)
    yield web_driver


# Add an Allure decorator to your test function
@allure.feature("Feature Name")
class TestYourClass:

    def capture_screenshot(self, test_name):
        screenshot_dir = "allure-screenshots"
        os.makedirs(screenshot_dir, exist_ok=True)
        screenshot_path = os.path.join(screenshot_dir, f"{test_name}.png")

        # Capture the screenshot using the driver passed from the fixture
        self.driver.save_screenshot(screenshot_path)

        # Attach the screenshot to the Allure report
        allure.attach.file(screenshot_path, name="Screenshot", attachment_type=allure.attachment_type.PNG)
