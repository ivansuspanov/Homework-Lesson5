from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def test_multiple_elements():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://httpbin.qa-territory.online/links/10")

        links = driver.find_elements(By.TAG_NAME, "a")

        assert len(links) == 9, (
            f"Ожидалось 9 ссылок, найдено: {len(links)}")

        for i, link in enumerate(links):
            assert link.is_displayed(), (
                f"Ссылка под индексом {i} не отображается")

        first_link_text = links[0].text
        assert "1" in first_link_text, (
            f"Текст первой ссылки должен содержать '1', "
            f"но был: '{first_link_text}'"
        )
    finally:
        driver.quit()
