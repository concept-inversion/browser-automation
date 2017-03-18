__author__ = 'santo'
from selenium import webdriver

from selenium.webdriver.common.keys import Keys


driver =webdriver.Chrome(executable_path=r'C:\Users\user\Documents\chromedriver\chromedriver.exe');
driver.implicitly_wait(1)
driver.maximize_window()

driver.get("http://www.bing.com/")
search=driver.find_element_by_id('sb_form_q')
search.clear()
search.send_keys('why is google faster than bing')
search.submit()

lists= driver.find_elements_by_class_name("a")

# get the number of elements found
print ('Found ' + str(len(lists)) + 'searches:')

# iterate through each element and print the text that is
# name of the search

i=0
for listitem in lists:
   print (listitem)
   i=i+1
   if(i>2):
      break


