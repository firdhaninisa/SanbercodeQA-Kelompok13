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

    def test_a_success_add_job_title(self):
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
            By.XPATH, "//div[2]/input").send_keys("Manager 4")  # isi job title
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[2]/div/div[2]/textarea").send_keys(
            "Office Work")  # isi description
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div/div[2]/div[2]/div/div/form/div[4]/div/div[2]/textarea").send_keys("Halo Pak")  # isi job note
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//button[@type='submit']").click()  # click save
        time.sleep(2)
        # driver.find_element(
        # By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[1]/h6").click()  # click pop up
        # driver.find_element(
        #     By.CSS_SELECTOR, ".oxd-toast-content").click()  # click pop up
        # time.sleep(4)

    # validasi
        # response_data = driver.find_element(
        #     By.XPATH, "//div[@id='oxd-toaster_1']/div/div/div[2]/p[2]").text

        # self.assertEqual('Success', response_data)

        response_data = driver.find_element(
            By.XPATH, "//div[@id='oxd-toaster_1']/div/div/div[2]/p[2]").text
        response_message = driver.find_element(
            By.XPATH, "//div[@id='oxd-toaster_1']/div/div/div[2]/p[2]").text

        self.assertIn('Success', response_data)
        self.assertEqual(response_message, 'Successfully Saved')

        #
        # response_data = driver.find_element(
        #     By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/div[1]/h6").text

        # self.assertEqual('Job Titles', response_data)

        # response_data = driver.find_element(
        #     By.XPATH, "//div[@id='app']/div/div/header/div/div/span/h6[2]").text

        # self.assertEqual('Admin', response_data)

        # response_url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList"

        # self.assertEqual(
        #     'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList'), response_url
        time.sleep(16)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
