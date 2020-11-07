import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:/Users/user/Downloads/er/chromedriver.exe')
driver.get("URL")
driver.maximize_window()

#Login_page
Logging = driver.find_element_by_xpath('//*[@id="login-view"]/form/div[1]/input')
Logging.send_keys('USERNAME')
Logging = driver.find_element_by_xpath('//*[@id="inputPassword"]')
Logging.click()
Logging.send_keys('PWD')
Logging = driver.find_element_by_xpath('//*[@id="login-view"]/form/div[3]/button')
Logging.click()
time.sleep(10)

#Selecting ISL Dashboard
Select = driver.find_element_by_xpath('/html/body/grafana-app/div/div/div/div/dashnav/div/div[1]/a')
Select.click()
time.sleep(10)
Select = driver.find_element_by_xpath('/html/body/grafana-app/div/div/div/div/dashnav/dashboard-search/div[2]/div[2]/div[1]/div/div[1]/dashboard-search-results/div[1]/div[3]/a[2]/span[2]/div')
Select.click()
time.sleep(5)

#Selecting BT Dashboard
driver.execute_script("window.open('https://monitor.hubble.in/d/144-hNAmk/bt-prod?refresh=10s&orgId=1');")
time.sleep(5)

#Creating function to loop
def loop():
    driver.switch_to_window(driver.window_handles[0])
    time.sleep(30)
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(15)

while True:
    loop()
