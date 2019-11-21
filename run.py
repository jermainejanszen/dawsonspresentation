import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = 'http://www.dawsonsespresso.com.au/'
driverPath = '/Users/jermaine/chromedriver'
chromeOptions = Options()
chromeOptions.headless = True

driver = webdriver.Chrome(driverPath, options=chromeOptions)
driver.get(url)

menuButton = driver.find_element_by_id('glfButton0')
menuButton.click()

time.sleep(5)

driver.switch_to.frame("gfOrderFrm")

menuItems = []

foundAllSpecials = False

counter = 0
while(not foundAllSpecials):
    itemName_element = driver.find_element_by_xpath(
        '//*[@id="fb-content"]/app-restaurant/div/ui-view/app-menu/div/app-menu-items/div[1]/div[3]/div[{}]/div[1]/div[1]/div[2]'.format(counter + 1))
    if(itemName_element.text == 'Hot Foods'):
        foundAllSpecials = True
        break
    menuItem = [None, None, None]
    menuItem[0] = itemName_element.text
    itemDescription_element = driver.find_element_by_xpath(
        '//*[@id="fb-content"]/app-restaurant/div/ui-view/app-menu/div/app-menu-items/div[1]/div[3]/div[{}]/div[1]/div[1]/div[3]'.format(counter + 1))
    menuItem[2] = itemDescription_element.text
    itemPrice_element = driver.find_element_by_xpath(
        '//*[@id="fb-content"]/app-restaurant/div/ui-view/app-menu/div/app-menu-items/div[1]/div[3]/div[{}]/div[1]/div[2]/div[1]/span'.format(counter + 1))
    menuItem[1] = itemPrice_element.text
    menuItems.append(menuItem)
    counter = counter + 1

for i in range(len(menuItems)):
    print('Item name: {}'.format(menuItems[i][0]))

driver.close()
