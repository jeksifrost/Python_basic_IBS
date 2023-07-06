from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def perform_google_search(keyword):
    driver.get("http://google.com/ncr")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(keyword)
    search_box.send_keys(Keys.RETURN)

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result-stats")))
    first_result = driver.find_element(By.CSS_SELECTOR, "#search .g a")
    assert first_result.get_attribute("href") == "https://selenide.org/", "First result is not selenide.org"

    images_link = driver.find_element(By.LINK_TEXT, "Images")
    images_link.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result-stats")))
    first_image = driver.find_element(By.CSS_SELECTOR, "#search .rg_i")
    assert "selenide.org" in first_image.get_attribute("href"), "First image is not related to selenide.org"

    all_link = driver.find_element(By.LINK_TEXT, "All")
    all_link.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "result-stats")))
    first_result_again = driver.find_element(By.CSS_SELECTOR, "#search .g a")
    assert first_result_again.get_attribute("href") == "https://selenide.org/", "First result has changed"

chrome_driver_path = "/path/to/chromedriver"  # Replace with the actual path to the Chrome WebDriver executable
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

perform_google_search("selenide")

driver.quit()