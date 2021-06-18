from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
PATH = 'C:/Program Files (x86)/SeleniumDrivers/chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://www.microsoft.com/en-us/')
driver.maximize_window()

class HomePage:
# header element x_path
    header_elements = {'O365': '/html/body/div[1]/div/div/header/div/div/nav/ul/li[1]/a',
                   'Office': '/html/body/div[1]/div/div/header/div/div/nav/ul/li[2]',
                   'Windows': '/html/body/div[1]/div/div/header/div/div/nav/ul/li[3]',
                   'Surface': '/html/body/div[1]/div/div/header/div/div/nav/ul/li[4]',
                   'XBox': '/html/body/div[1]/div/div/header/div/div/nav/ul/li[5]',
                   'Deals': '/html/body/div[1]/div/div/header/div/div/nav/ul/li[6]/a',
                   'Support': '/html/body/div[1]/div/div/header/div/div/nav/ul/li[7]/a'
                   }
    print('Checking header buttons... \n')
    for element in header_elements.keys():
        if driver.find_element_by_xpath(header_elements[element]):
            print(element, 'button present')
    windows_button = driver.find_element_by_xpath(header_elements['Windows'])
    webdriver.ActionChains(driver).move_to_element(windows_button).click(windows_button).perform()

class WindowsPage:
    # find Windows 10 dropdown menu and print elements
    windows10_xpath = '/html/body/span[2]/div/div/div/header/div/div/nav/ul/li[2]'
    windows10_button = driver.find_element_by_xpath(windows10_xpath)
    webdriver.ActionChains(driver).move_to_element(windows10_button).click(windows10_button).perform()
    time.sleep(2)
    windows10_dropdown_selector = '#uhf-g-nav > ul > li:nth-child(2) > div > ul'
    windows10_dropdown_elements = driver.find_elements_by_css_selector(windows10_dropdown_selector)
    print('Verifying Windows10 dropdown items...\n')
    for element in windows10_dropdown_elements:
        print(element.text)
    #find search button and search for Visual Studio
    search_xpath = '/html/body/span[2]/div/div/div/header/div/div/div[4]/form/button'
    search_button = driver.find_element_by_xpath(search_xpath)
    webdriver.ActionChains(driver).move_to_element(search_button).click(search_button).perform()
    time.sleep(3)
    search_input_xpath = '/html/body/span[2]/div/div/div/header/div/div/div[4]/form/input'
    search_input = driver.find_element_by_xpath(search_input_xpath)
    webdriver.ActionChains(driver).move_to_element(search_input).click(search_input).perform()
    search_input.send_keys('visual studio')
    webdriver.ActionChains(driver).move_to_element(search_button).click(search_button).perform()
class VSProductPage:
    #find xpath correlating to price of first 3 elements
    price1_xpath = '/html/body/div[2]/section/div[1]/div[1]/div[3]/div/div/ul/li[1]/div/a/div[2]/div/div/span[3]/span[1]'
    price2_xpath = '/html/body/div[2]/section/div[1]/div[1]/div[3]/div/div/ul/li[2]/div/a/div[2]/div/div/span[3]/span[1]'
    price3_xpath = '/html/body/div[2]/section/div[1]/div[1]/div[3]/div/div/ul/li[3]/div/a/div[2]/div/div/span[3]/span[1]'
    price1 = driver.find_element_by_xpath(price1_xpath).text
    price2 = driver.find_element_by_xpath(price2_xpath).text
    price3 = driver.find_element_by_xpath(price3_xpath).text
    print('Search Result Prices:', '\n1st item price:', price1, '\n2nd item price:', price2, '\n3 rd Item Price:', price3)
    #shorten text to integer only
    price1 = price1[1:]
    price1 = price1.replace(",","")
    print('VSProductPage price:', price1)
    product1_xpath = '/html/body/div[2]/section/div[1]/div[1]/div[3]/div/div/ul/li[1]/div/a/div[1]'
    product1_button = driver.find_element_by_xpath(product1_xpath)
    webdriver.ActionChains(driver).move_to_element(product1_button).click(product1_button).perform()
class VSProduct1Page:
    product1price_xpath = '/html/body/section/div[1]/div[1]/div[1]/div[2]/div[6]/div/div[1]'
    product1price = driver.find_element_by_xpath(product1price_xpath).text
    product1price = product1price[1:]
    product1price = product1price.replace(',','')
    print('VSProduct1Page price:', product1price)
    if product1price == VSProductPage.price1:
        print('prices are equal')
    x_button_xpath = '/html/body/div[3]/div[3]/div[1]'
    x_button = driver.find_element_by_xpath(x_button_xpath)
    webdriver.ActionChains(driver).move_to_element(x_button).click(x_button).perform()
    addtocart_xpath = '/html/body/section/div[1]/div[1]/div[1]/div[2]/div[6]/div/div[3]/div/div/div/div[2]/button'
    addtocart_button = driver.find_element_by_xpath(addtocart_xpath)
    webdriver.ActionChains(driver).move_to_element(addtocart_button).click(addtocart_button).perform()


class ProductCartPage:
    product1_cartprice_xpath = '/html/body/section/div[1]/div[1]/div[1]/div[2]/div[6]/div/div[1]'
    product1_cartprice = driver.find_element_by_xpath(product1_cartprice_xpath).text
    product1_cartprice = product1_cartprice[1:]
    product1_cartprice = product1_cartprice.replace(',','')
    print('Product1CartPage price:', product1_cartprice)
    if product1_cartprice == VSProductPage.price1 and product1_cartprice == VSProduct1Page.product1price:
        print('prices are all equal')

    time.sleep(5)
    # quantity20_xpath = '//*[@id="store-cart-root"]/div/div/div/section[1]/div/div/div/div/div/div[2]/div[2]/div[1]'
    # quantity20_selection = driver.find_element_by_xpath(quantity20_xpath)
    quantity_selection = driver.find_element_by_css_selector("#store-cart-root > div > div > div > section.main--1-Tv4Wkw > div > div > div > div > div > div.item-details > div.item-quantity-price > div.item-quantity > select")
    webdriver.ActionChains(driver).move_to_element(quantity_selection).click(quantity_selection).perform()
    select_quantity = Select(quantity_selection)
    select_quantity.select_by_value('20')
    time.sleep(3)
    product_qty_cartprice_xpath = '/html/body/section/div[1]/div/div/div/div/div/section[2]/div/div/div[1]/div/span[1]/span[2]/div/span/span[2]/span'
    product_qty_cartprice = driver.find_element_by_xpath(product_qty_cartprice_xpath).text
    product_qty_cartprice = product_qty_cartprice[1:]
    product_qty_cartprice = product_qty_cartprice.replace(',','')
    print(product_qty_cartprice)
    if float(product_qty_cartprice) == float(product1_cartprice)*20.0:
        print('Quantified price is equal to product price * quantity')
    else:
        print('Failed to verify Quantified Price')
time.sleep(3)


driver.quit()