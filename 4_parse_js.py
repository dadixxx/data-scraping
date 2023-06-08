 
import  requests 

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.implicitly_wait(10) # seconds

url = "https://www.woolworths.com.au/shop/productdetails/84552/coca-cola-classic-soft-drink-multipack-cans"

driver.get(url)

elements = driver.find_elements(By.XPATH, '/html/body/ar-partial/ar-product-detail-container/section/div[1]/div[2]/div[2]/ar-product-detail-panel/section/div[1]/div[1]/ar-product-price/div/div[1]/div/span[2]')
print(elements)
for elt in elements:
   print(elt.text)

driver.quit()

