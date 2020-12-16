from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from bs4 import BeautifulSoup

DRIVER_PATH = '/Users/jasonbeedle/Desktop/snaviescraper/chromedriver'
driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get("http://best4sport.tv/extra")
results = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
    (By.CSS_SELECTOR, ".program1_content_container")))
soup = BeautifulSoup(results.get_attribute("outerHTML"), 'html.parser')
program_time = []
sport = []
program_text = []
program_info = []
for item in soup.select(".program_details "):
    if item.find_next(class_='program_time'):
        program_time.append(item.find_next(
            class_='program_time').text.strip())
    else:
        program_time.append("Nan")
    if item.find_next(class_='sport'):
        sport.append(item.find_next(class_='sport').text.strip())
    else:
        sport.append("Nan")
    if item.find_next(class_='program_text'):
        program_text.append(item.find_next(class_='program_text').text.strip())
    else:
        program_text.append("Nan")
    if item.find_next(class_='program_info'):
        program_info.append(item.find_next(class_='program_info').text.strip())
    else:
        program_info.append("Nan")

df = pd.DataFrame({"program_time": program_time, "sport": sport,
                   "program_text": program_text, "program_info": program_info})
print(df)
df.to_csv("sportExtra.csv")
