# ************************** man hinh loai 2 *************************
import sys
import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from info import ps, ids
service = Service(executable_path=ChromeDriverManager().install())


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.driver = None
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        self.uic.pushButton.clicked.connect(self.run_sele)

    def run_sele(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.facebook.com")
        # elem = self.driver.find_element(By.XPATH, '//*[@id="email"]')
        elem = self.driver.find_element(By.ID, "email")
        elem.send_keys(ids)
        # elem = self.driver.find_element(By.XPATH, '//*[@id="pass"]')
        elem = self.driver.find_element(By.ID, "pass")
        elem.send_keys(ps)
        elem = self.driver.find_element(By.NAME, "login")
        elem.click()
        time.sleep(1)
        self.driver.get("https://www.facebook.com/nhi.phan.583")
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0,1000)")
        print("click class")
        # elem_1 = self.driver.find_element(By.XPATH, r"""//span[text()='Friends']""")
        elem = self.driver.find_element(By.XPATH, """//span[text()="Like"]""")
        time.sleep(1)
        elem.click()

    def closeEvent(self, event):
        self.driver.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())


