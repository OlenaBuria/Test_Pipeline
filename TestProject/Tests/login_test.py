from selenium import webdriver
import time
import unittest
import HtmlTestRunner
import moment
import allure
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from TestProject.Pages.loginPage import LoginPage
from TestProject.Pages.homePage import HomePage



class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):

        # cls.driver = webdriver.Firefox(executable_path="/Users/elenaburiakova/PycharmProjects/Selenium/Drivers/geckodriver")
        cls.driver = webdriver.Chrome(executable_path="/Users/elenaburiakova/PycharmProjects/Selenium/Drivers/chromedriver")
        cls.driver.implicitly_wait(10)

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/")

        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            time.sleep(4)
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error is occurred")
            print(error)
            curr_time = moment.now().strftime("%H-%M-%S_%d-%m-%Y")
            screenshot_name = "screenshot_"+curr_time
            allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                          attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("There was an exception")
            raise

        else:
            print("No exception occurred")

        # self.driver.find_element_by_id("txtUsername").send_keys("Admin")
        # self.driver.find_element_by_id("txtPassword").send_keys("admin123")
        # self.driver.find_element_by_id("btnLogin").click()
        # self.driver.find_element_by_id("welcome").click()
        # self.driver.find_element_by_link_text("Logout").click()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):

        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

if __name__ == '__main__':
   unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="/Users/elenaburiakova/PycharmProjects/Selenium/Drivers/Reports"))
