import os
import time
import requests
from datetime import date, datetime
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def grab_page_selenium(url):
    chromeOptions = webdriver.chrome.options.Options()
    #chromeOptions.add_argument('--headless')
    chromeOptions.add_experimental_option("detach", True)
    chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)
    WebDriverWait(driver, timeout=600).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'footer.footer')))

    errors = driver.find_elements(By.CSS_SELECTOR, "div#cf-error-details")
    for error in errors:
        code = error.find_elements(By.CSS_SELECTOR, 'header h2')
        if len(code) == 0:
            code = error.find_elements(By.CSS_SELECTOR, 'h1')
        code = code[0].text
        
        desc = error.find_elements(By.CSS_SELECTOR, 'section div#what-happened-section p')
        if len(desc) == 0:
            desc = error.find_elements(By.CSS_SELECTOR, 'h2.cf-subheadline')
        desc = desc[0].text
        
        raise Exception(f'{code}: {desc}')


    content = driver.find_element(By.ID, 'pb-page-content')
    content = '<html>' + content.get_attribute("outerHTML") + '</html>'
        
    driver.quit()
    return content


def grab_page(url):
    session = requests.session()
    session.headers = {'User-Agent': UserAgent().random}
    
    data = session.get(url).text
    return data

def grab_paper(url):
    data = grab_page(url)
    soup = BeautifulSoup(data, 'html.parser')

    error = soup.select_one('div#cf-error-details')
    if error != None:
        code = error.select_one('header h2')
        if code == None:
            code = error.select_one('h1')
        code = code.text
        
        desc = error.select_one('section div#what-happened-section p')
        if desc == None:
            desc = error.select_one('h2.cf-subheadline')
        desc = desc.text
        
        raise Exception(f'{code}: {desc}')

    return data

def grab_paper_with_retries(url, sleeptime=30):
    while True:
        try:
            data = grab_paper(url)
            time.sleep(sleeptime)
            return data
        except Exception as e:
            print(e)
            print('Waiting 5 min before retrying...')
            time.sleep(60 * 5)

def grab_series(url):
    return grab_page_selenium(url)

def grab_series_with_retries(url, sleeptime=30):
    return grab_paper_with_retries(url, sleeptime)

def grab_conference(url):   
    chromeOptions = webdriver.chrome.options.Options()
    #chromeOptions.add_argument('--headless')
    chromeOptions.add_experimental_option("detach", True)
    chromeOptions.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})

    driver = webdriver.Chrome(options=chromeOptions)
    driver.get(url)
    WebDriverWait(driver, timeout=600).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'footer.footer')))
    print('initial load completed')

    # dismiss cookie banner if necessary
    elements = driver.find_elements(By.CSS_SELECTOR, 'button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
    for e in elements:
        e.click()
        time.sleep(1)    

    wait = WebDriverWait(driver, timeout=20, poll_frequency=0.5)
    elements = driver.find_elements(By.CSS_SELECTOR, "div.item-meta a.removed-items-count")
    for e in elements:
        driver.execute_script("arguments[0].dispatchEvent(new MouseEvent('mousedown', {bubbles:true}));", e)
        time.sleep(1)
    elements = driver.find_elements(By.CSS_SELECTOR, "button.item-meta a.removed-items-count")
    for e in elements:
        e.click()
        time.sleep(1)

    time.sleep(10)

    collapsed = driver.find_elements(By.CSS_SELECTOR, "div.toc__section > a[aria-expanded='false']")
    if len(collapsed) > 0:
        print('Clicking on all sections...')
        for link in collapsed:
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            driver.execute_script("arguments[0].click();", link)
            time.sleep(10)
        print('Waiting for all sections to load...')
        WebDriverWait(driver, timeout=600, poll_frequency=1).until(EC.none_of(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.lazy-loaded'))))
        print('Done loading sections')

    elements = driver.find_elements(By.CSS_SELECTOR, "button.showAllProceedings")
    for e in elements:
        print('lazy loading rest of papers')
        driver.execute_script("arguments[0].scrollIntoView(true);", e)
        driver.execute_script("arguments[0].click();", e)

        while True:
            loader = driver.find_elements(By.CSS_SELECTOR, "div.table-of-content div.see_more div.not-loaded")
            if len(loader) == 0:
                break
            driver.execute_script("arguments[0].scrollIntoView(true);", loader[0])           
            time.sleep(1)
            WebDriverWait(driver, timeout=60, poll_frequency=1).until(lambda x: 'not-loaded' not in loader[0].get_attribute('class'))
        

    content = driver.find_element(By.ID, 'pb-page-content')
    content = '<html>' + content.get_attribute("outerHTML") + '</html>'
        
    driver.quit()
    return content

if __name__ == '__main__':
    #grab_paper('https://dl.acm.org/doi/10.1145/67449.67479')
    #grab_page_selenium('https://dl.acm.org/doi/10.1145/67449.67479')
    #grab_conference('https://dl.acm.org/doi/proceedings/10.1145/3173574')
    print(grab_page('https://en.wikipedia.org/wiki/Conference_on_Human_Factors_in_Computing_Systems'))
