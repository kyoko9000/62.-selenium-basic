import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from info import ids, ps

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com")
elem = driver.find_element(By.ID, "email")
elem.send_keys(ids)
elem = driver.find_element(By.ID, "pass")
elem.send_keys(ps)
elem = driver.find_element(By.NAME, "login")
elem.submit()
# elem.click()
#
# time.sleep(1)
# driver.get("https://www.facebook.com/profile.php?id=100084521482536")
# time.sleep(2)
# driver.execute_script("window.scrollBy(0,1200)")
# elem = driver.find_element(By.XPATH, """//p[@class='kmwttqpk kjdc1dyq l7ghb35v m8h3af8h']""")
# elem.send_keys("chào bạn")
# elem.send_keys(Keys.RETURN)
time.sleep(20)
driver.close()