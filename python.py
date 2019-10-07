#под комментами для проверки xpath
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://suninjuly.github.io/simple_form_find_task.html")
#driver.get("http://suninjuly.github.io/find_xpath_form")
formcontrol=driver.find_element_by_css_selector(".form-control")
formcontrol.send_keys("Nika")
lastname=driver.find_element_by_name("last_name")
lastname.send_keys("Pospielova")
firstname=driver.find_element_by_name("firstname")
firstname.send_keys("Sever")
country=driver.find_element_by_id("country")
country.send_keys("Ukraine")
submitbutton=driver.find_element_by_id("submit_button")
#submitbutton=driver.find_element_by_xpath("//button[text()='Submit']")
submitbutton.click()
time.sleep(10)
