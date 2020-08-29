from selenium import webdriver
import time
import pandas
month = input("give the month :")
year = input("give the year:")
high=[]
low=[]
precep=[]
month = month.lower()
browser = webdriver.Firefox(executable_path='./geckodriver')
url = 'https://www.accuweather.com/en/in/kolkata/206690/'+month+'-weather/206690?year='+year+'&view=list'
browser.get(url)
time.sleep(4)
for i in browser.find_elements_by_class_name('high'):
    high.append(int(i.text[:-1]))
for i in browser.find_elements_by_class_name('low'):
    low.append(int(i.text[2:-1]))
for i in browser.find_elements_by_xpath('//div[@class="info precip"]/p[2]'):
    precep.append(float(i.text[:-3]))
browser.quit()
date = list(range(len(high)+1))[1:]

dic = {"date":date,"highest Temparature":high,"lowest Temprature": low ,"precipitation":precep}

df = pandas.DataFrame(dic)

df.to_csv('weather_'+month+year+'.csv',index=False)