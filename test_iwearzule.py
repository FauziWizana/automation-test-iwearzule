from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest
import pyautogui

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://iwearzule.com")
    yield driver
    driver.quit()

def test_login_until_success(driver):
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.find_element_by_css_selector("#navbar-collapse > ul.nav.navbar-nav.navbar-nav-iwzl.navbar-right > li:nth-child(3) > a.link-menu-right.link-register.count-menu").click()
    time.sleep(1)
    driver.find_element_by_id("txtFullName").send_keys("mike")
    time.sleep(1)
    driver.find_element_by_id("txttgllahir").click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[30]/div[1]/table/tbody/tr[2]/td[2]').click()
    time.sleep(1)
    driver.find_element_by_id("txtPhone").send_keys("08811223344")
    time.sleep(1)
    driver.find_element_by_id("txtEmailRegist").send_keys("mike@gmail.com")
    time.sleep(1)
    driver.find_element_by_id("txtPasswordRegist").send_keys("passwordrahasia")
    time.sleep(1)
    driver.find_element_by_id("txtConfPassword").send_keys("passwordrahasia")
    time.sleep(1)
    driver.find_element_by_id("btnSignup").click()

    ActionChains(driver).move_to_element((driver.find_element_by_id("menuUser"))).perform()
    time.sleep(1)
    driver.find_element_by_link_text("DASHBOARD").click()
    time.sleep(5)
    driver.find_element_by_id("profile-picture").click()
    time.sleep(2)
    pyautogui.write(r"C:\Users\ACER\Documents\monster.jpg")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(5)