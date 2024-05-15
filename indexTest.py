# imports
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# set driver
driver = webdriver.Chrome()
driver.get()
# functions
def elementOne():
    elementOne = driver.find_element(By.ID, value="element-one")
    elementOne.click()
    assert "box1style" in elementOne.get_attribute("class")
    driver.save_screenshot("element-one.png")
def elementTwo():
    elementTwo =driver.find_element(By.ID, value="element-two")
    ActionChains(driver).double_click(elementTwo).perform()
    driver.save_screenshot("element-two.png")
    

def elementThree():
    elementThree=driver.find_element(By.ID, value="element-three")
    ActionChains(driver).move_to_element(elementThree).perform()
    driver.save_screenshot("element-three.png")
def elementFour():
    elementFour=driver.find_element(By.ID, value="element-four")
    elementFour.click()
    driver.save_screenshot("element-four.png")
    


# test1()
elementOne()
# time.sleep(0.1)
time.sleep(0.1)
# test2()
elementTwo()
# time.sleep(0.1)
time.sleep(0.1)
# test3()
elementThree()
# time.sleep(0.1)
time.sleep(0.1)
# test4()
elementFour()
# time.sleep(0.1)
time.sleep(0.1)
# test5()

driver.close()