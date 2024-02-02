import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
      
        
    def test_a_success_login(self):
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
        driver.find_element(By.CLASS_NAME, "oxd-main-menu-item--name").click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[2]').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div/button').click()
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input').send_keys("Toronto Office")
        time.sleep(1)
        
        select_Timeperiod = Select(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]'))
        select_Timeperiod.select_by_visible_text("Canada")
        #driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div/div[1]').send_keys("Canada")
        time.sleep(1)

        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]').click()
        time.sleep(1)


        # wait for dashboard page to load
        #wait = WebDriverWait(driver, 10)
        #wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "page-title")))

    #validasi
        response_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveLocations"
        self.assertEqual('https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveLocations', response_url)

        #self.assertEqual('https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/indexpython', response_url)
        #response_data = driver.find_element(By.CLASS_NAME,"oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module").text
        #response_data = driver.find_element(By.XPATH,"//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
        #self.assertIn('Dashboard', response_data)
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()