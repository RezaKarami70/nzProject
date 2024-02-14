import time
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""Opening web page using web driver"""
print("Opening page")
driver = webdriver.Chrome()
url = ("https://www.immigration.govt.nz/new-zealand-visas/preparing-a-visa-application/working-in-nz/qualifications"
       "-for-work/green-list-occupations")
driver.get(url)
time.sleep(1)

"""Accepting popup baner for cookies"""
print("Accepting cookies")
WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#inz_cookie_consent_banner button"))).click()

try_num = 1
"""loading all jobs with click on see more"""
while True:
    try:
        driver.find_element(by=By.CLASS_NAME, value="results_loadbtn").click()
        print("Try " + str(try_num))
        try_num += 1
        time.sleep(1)

    except:
        print("No more Try")
        break

"""Scraping data from loaded page"""
html = driver.page_source.encode("utf-8")
page_soup = soup(driver.page_source, 'html5lib')
containers = page_soup.findAll(
    "h3", {"class": "content_list_heading"})

num_job = 1

with open("Jobs.txt", "w",encoding="utf-8") as file:
    for container in containers:
        file.write(str(num_job)+","+container.text+"\n")
        num_job += 1
    file.close()

driver.quit()
print("END!")
