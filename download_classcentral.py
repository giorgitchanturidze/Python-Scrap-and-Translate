import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

url = "https://www.classcentral.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Download the page HTML using requests and BeautifulSoup
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

# Download the page JavaScript and CSS using Selenium
driver = webdriver.Firefox()  # You will need to download the appropriate driver for your browser
driver.get(url)
time.sleep(10)  # Wait for the page to load
# Find all elements on the page using the  "//*"
elements = driver.find_elements(By.XPATH, "//*")
# Iterate over the elements and hover over each one
for element in elements:
    try:
        ActionChains(driver).move_to_element(element).perform()
        time.sleep(0.1)
    except:
        pass
# Iterate over the elements and click each one
for element in elements:
    try:
        element.click()
        time.sleep(0.1)
    except:
        pass
# Get the updated HTML
html = driver.page_source

driver.quit()

# Parse the JavaScript and CSS using BeautifulSoup
soup2 = BeautifulSoup(html, "html.parser")


# Save the HTML, JavaScript, and CSS content to files
with open("classcentral.html", "w") as f:
    f.write(str(soup))

