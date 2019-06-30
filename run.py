from selenium import webdriver

url = 'http://www.dawsonsespresso.com.au/'
# driverPath = '/Users/jermaine/Desktop/chromedriver'
driverPath = 'C:/Users/User/Desktop/chromedriver'

driver = webdriver.Chrome(driverPath)
driver.get(url)

menuButton = driver.find_element_by_id('glfButton0')
menuButton.click()

numSpecials = input('How many specials are there today?\n')
numSpecials = int(numSpecials)
print(numSpecials)

menuItems = [[None for x in range(numSpecials)] for y in range(numSpecials)]


for i in range(numSpecials):
    itemName_element = driver.find_element_by_xpath('//*[@id="fb-content"]/app-restaurant/div/ui-view/app-menu/div/app-menu-items/div[1]/div[3]/div[{}]/div[1]/div[1]/div[2]'.format(i + 1))
    menuItems[i][0] = itemName_element.text
    itemDescription_element = driver.find_element_by_xpath('//*[@id="fb-content"]/app-restaurant/div/ui-view/app-menu/div/app-menu-items/div[1]/div[3]/div[{}]/div[1]/div[1]/div[3]'.format(i + 1))
    menuItems[i][2] = itemDescription_element.text
    itemPrice_element = driver.find_element_by_xpath('//*[@id="fb-content"]/app-restaurant/div/ui-view/app-menu/div/app-menu-items/div[1]/div[3]/div[{}]/div[1]/div[2]/div[1]/span'.format(i + 1))
    menuItems[i][1] = itemPrice_element.text

for i in range(numSpecials):
    print(menuItems[i][0])

driver.close()
