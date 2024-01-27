from selenium import webdriver
import pytest


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    request.cls.driver = driver
    yield
    driver.quit()
