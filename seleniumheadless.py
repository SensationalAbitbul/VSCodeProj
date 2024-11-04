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
driver.get("https://google.com")
#driver = webdriver.Chrome('/snap/chromium/2985/usr/lib/chromium-browser/chromedriver')
WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "gLFyf"))
)

input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("Rick Roll" + Keys.ENTER)

WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "Rick"))
)


link = driver.find_element(By.PARTIAL_LINK_TEXT, "Rick")
link.click() 

time.sleep(10)
print(driver.current_url)
driver.quit()
