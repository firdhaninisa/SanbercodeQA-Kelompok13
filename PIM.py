import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
      
        
    def test_PIM_search(self):
        #step
        driver = self.browser #buka web browser
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login") #buka situs
        time.sleep(3)        
        driver.find_element(By.NAME, "username").send_keys("Admin") #isi email
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys("admin123") #isi password
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys('Garry')
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()
        time.sleep(1)
       
       
    #validasi
        response_url = "https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList"
        self.assertEqual('https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList', response_url)

            
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()