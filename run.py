import time
import urllib
import urllib.request
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

items = driver.find_elements_by_xpath(
    '//*[@id="fb-content"]/app-restaurant/div/ui-view/app-menu/div/app-menu-items/div[1]/div[3]')
itemsInfo = items[0].text.split('\n')

itemImages = []
for i in range(6):
    try:
        item = driver.find_element_by_xpath(
            '//*[@id="fb-content"]/app-restaurant/div/ui-view/app-menu/div/app-menu-items/div[1]/div[3]/div[{}]/div/div[1]/div[1]'.format(i + 1))
        itemImages.append(item.get_attribute('style')[23:-3])
    except:
        break

for i in range(int(len(itemsInfo)/3)):
    menuItem = {
        'name': itemsInfo[i*3], 'description': itemsInfo[i*3 + 1], 'price': itemsInfo[i*3 + 2]}
    if 'Salad' not in menuItem['name']:
        menuItems.append(menuItem)

for i in range(len(menuItems)):
    print('Item name: {}'.format(menuItems[i]['name']))
    print('Item description: {}'.format(menuItems[i]['description']))
    print('Item price: {}'.format(menuItems[i]['price']))
    urllib.request.urlretrieve(itemImages[i], "images/{}.jpg".format(i + 1))

driver.close()
