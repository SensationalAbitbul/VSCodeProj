from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options

service = Service(executable_path=r'/usr/bin/chromedriver')
options = Options() #webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument("--disable-dev-shm-using")
options.add_argument("--remote-debugging-port=9222")
options.add_argument('--disable-crash-reporter')
options.add_argument('--no-sandbox')
driver = webdriver.Chrome(service=service, options=options)
#driver.get("https://google.com")
#driver = webdriver.Chrome('/snap/chromium/2985/usr/lib/chromium-browser/chromedriver')
driver.get("file:///srv/VSCodeProj-main/Elnet/Elnet/ElnetPhases.html")
time.sleep(5)
ids = driver.find_elements(By.XPATH, './/tr')
#ids1 = driver.find_elements(By.ID, 'n0')
# to get names use '//*[@name]'
for ii in ids:
    #print('Tag: ' + ii.tag_name)
    print('ID: ' + ii.get_attribute('id'))     # element id as string
    #print('Name: ' + ii.get_attribute('name')) # element name as string
#for e in ids1:
#    print(e.text)
#WebDriverWait(driver, 5).until(
#    EC.presence_of_all_elements_located((By.CLASS_NAME, "gLFyf"))
#)
#WebDriverWait(driver, 5).until(
#    EC.presence_of_all_elements_located((By.ID, "back"))
#)
#
#input_element.clear()
#input_element.send_keys("Rick Roll" + Keys.ENTER)s
#
#WebDriverWait(driver, 10).until(
#    EC.presence_of_all_elements_located((By.LINK_TEXT, "Main screen"))
#)
#
#
#link = driver.find_element(By.PARTIAL_LINK_TEXT, "here")
#link.click() 
#time.sleep(10)
#print(link)
#print(driver.current_url)
#print(driver.current_url)
driver.quit()
