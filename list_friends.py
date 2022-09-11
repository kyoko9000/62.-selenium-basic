import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from info import ids, ps

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com")
elem = driver.find_element(By.ID, "email")
elem.send_keys(ids)
elem = driver.find_element(By.ID, "pass")
elem.send_keys(ps)
elem = driver.find_element(By.NAME, "login")
elem.click()
time.sleep(1)
driver.get("https://www.facebook.com/profile.php?id=100034077260467&sk=friends")
time.sleep(5)
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(5)
    elem = driver.find_elements(By.XPATH, "//span [@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 "
                                          "gem102v4 ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 szxhu1pg "
                                          "hpj0pwwo sggt6rq5 innypi6y pbevjfx6']")
    print(len(elem))
    if len(elem) > 29:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        break
time.sleep(5)
elem = driver.find_elements(By.XPATH, "//span [@class='gvxzyvdx aeinzg81 t7p7dqev gh25dzvf exr7barw b6ax4al1 gem102v4 "
                                      "ncib64c9 mrvwc6qr sx8pxkcf f597kf1v cpcgwwas m2nijcs8 szxhu1pg hpj0pwwo "
                                      "sggt6rq5 innypi6y pbevjfx6']")
for i in elem:
    print(i.text)
time.sleep(5)
driver.quit()

