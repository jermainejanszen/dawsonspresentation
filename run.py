from selenium import webdriver

url = 'http://www.dawsonsespresso.com.au/'

driver = webdriver.Chrome('/Users/jermaine/Desktop/chromedriver')
driver.get(url)

menuButton = driver.find_element_by_id('glfButton0')
menuButton.click()

numSpecials = input('How many specials are there today?\n')
numSpecials = int(numSpecials)
print(numSpecials)


menuItems = driver.find_elements_by_class_name('m-items')

for i in range(0, numSpecials):
    print(menuItems)

driver.close()
