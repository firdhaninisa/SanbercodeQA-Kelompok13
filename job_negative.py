import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_b_job_title_already_exists(self):
        # step
        driver = self.browser  # buka web browser
        # buka situs
        driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys(
            "Admin")  # isi email
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(
            "admin123")  # isi password
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div/div/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a/span").click()  # buka admin page
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div/header/div[2]/nav/ul/li[2]/span/i").click()  # click job
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//a[contains(text(),'Job Titles')]").click()  # open job title page
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div/button").click()  # add button
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[2]/input").send_keys("Manager")  # isi job title
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@type='submit']").click()  # click save
        time.sleep(2)

    # validasi
        response_data = driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/span').text

        self.assertEqual('Already exists', response_data)
        time.sleep(4)

    def test_c_job_title_empty(self):
        # step
        driver = self.browser  # buka web browser
        # buka situs
        driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(3)
        driver.find_element(By.NAME, "username").send_keys(
            "Admin")  # isi email
        time.sleep(1)
        driver.find_element(By.NAME, "password").send_keys(
            "admin123")  # isi password
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div/div/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div/aside/nav/div[2]/ul/li/a/span").click()  # buka admin page
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div/header/div[2]/nav/ul/li[2]/span/i").click()  # click job
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//a[contains(text(),'Job Titles')]").click()  # open job title page
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/div/div/button").click()  # add button
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[2]/input").send_keys("")  # isi job description
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@type='submit']").click()  # click save
        time.sleep(2)

    # validasi
        response_data = driver.find_element(
            By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/span').text

        self.assertEqual('Required', response_data)
        time.sleep(4)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
