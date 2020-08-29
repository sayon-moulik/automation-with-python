from selenium import webdriver
import urllib.request
instaID = input("give the insta ID:")
browser = webdriver.Firefox(executable_path='./geckodriver')
instaHnadler = "https://www.instagram.com/"+instaID
insta=browser.get(instaHnadler)
try:
    image = browser.find_element_by_xpath('//img[@class="_6q-tv"]')
except:
        image = browser.find_element_by_xpath('//img[@class="be6sR"]')
imagelink = image.get_attribute('src')
urllib.request.urlretrieve(imagelink,'./'+instaID+'.jpeg')