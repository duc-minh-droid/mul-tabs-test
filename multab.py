from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import template  
from time import *
import os

# set up
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(5)
driver.get("https://chrome.google.com")

# fake data
fake_data = ["All my tears", "Shave the bread", "Break the beans"]

# open tabs
opened_tabs = 0
for idx, data in enumerate(fake_data):
    html_data = template.generateTemplate(data)
    file_name = data.split(' ')[0].lower() + '.html'
    with open("templates/"+file_name, 'w') as file:
        file.write(html_data)
        file.close()
    file_src = 'file://' + os.getcwd() + '/templates/' + file_name
    driver.execute_script('window.open("","_blank");')
    driver.switch_to.window(driver.window_handles[len(driver.window_handles)-1])
    driver.get(file_src)
    
    # data processing
    print(driver.title)
    driver.save_screenshot(f"images/screenshot{opened_tabs}.png")
    
    # end processing
    opened_tabs+=1
    
# close tabs
for i in range(opened_tabs):
    driver.switch_to.window(driver.window_handles[1])
    driver.close()

while True:
    pass