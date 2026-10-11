from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_form_submission():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        url = "https://httpbin.qa-territory.online/forms/post"
        driver.get(url)

        driver.find_element(By.NAME, "custname").send_keys("Ivan")

        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Submit')]").click()

        assert driver.current_url != url, (
            f"URL не изменился: {driver.current_url}")

    finally:
        driver.quit()
