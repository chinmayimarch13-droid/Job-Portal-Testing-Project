from selenium import webdriver
from selenium.wedbriver.common.by import By
driver = webdriver.chrome()
driver.get("http://example.com/login")
driver.find_element(By.NAME,"username").send_keys("testuser")
driver.find_element(By.NAME,"password").send_keys("1234")
driver.find_element(By.ID,"login").click()
print("Login test executed")
driver.quit()
