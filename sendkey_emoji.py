import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
service = Service(executable_path=ChromeDriverManager().install())


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=service)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.facebook.com")
    #     self.assertIn("Python", driver.title)
        elem = driver.find_element(By.ID, "email")
        elem.send_keys("pycon")
        elem = driver.find_element(By.ID, "pass")
        elem.send_keys("dfgdfg")
        elem = driver.find_element(By.NAME, "login")
        # elem.click()
    #     elem.send_keys(Keys.RETURN)
    #     self.assertNotIn("No results found.", driver.page_source)
    #
    # def tearDown(self):
    #     self.driver.close()


if __name__ == "__main__":
    unittest.main()