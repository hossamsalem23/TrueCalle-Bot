#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from time import sleep
from random import randint
from getpass import getpass
from PIL import Image



#close
print('TrueCaller Selenuim auto search')
print('\033[34m' + 'Made by [hossam salem]' )
print('\033[34m' + 'https://www.facebook.com/Hossam.salem55' )
logo = '''


                                                                    .oo.  /o+                       
  -/.                                                               .oo-  /o+                       
`-oo:``   ``....`  ```     ``     `....`       `....`      `....`   .oo-  /o+     `....`     ``....`
-:oo/--  .++/-:+/` +o/    .oo-  `/+:-:/+/.   ./+/::/+/`  ./+:-:++:  .oo-  /o+   .//:-:++:`  :++--/+:
 .oo-    -oo.  ``  +o/    .oo- `++-`..-+o+` .++.   `:/.  .:-   /o+  .oo-  /o+  -++.`..:oo/  /o+   ` 
 .oo-    -oo.      +o/    .oo- -o+:::--..`  :o+           `.-::+o+  .oo-  /o+  /o+::---..`  /o+     
 .oo-    -oo.      +o/    .oo- -o+`         :o+`     _   /+/.``:o+  .oo-  /o+  /o/      `-  /o+     
 .oo:    -oo.      /o+`   -oo-  /o+-.`.-++` `/o+-``.:+- .oo-   /o+  .oo-  /o+  `+o/-``.:+:  /o+     
  -/+//` .++`      `:/+++++/-    ./++++/-     -/++++:.   -/++/++/-  .++.  :+/   `-/++++/.   :+/     
'''
print('\033[31m' + logo + '\033[31m')
sleep(3)
print('Use Mircosoft Account ')
print('========================== ')
user = input( '\033[32m' + "Email Address : ")
password =  getpass()
num = input( "Phone Number : ")

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome()
driver.implicitly_wait(15) # seconds

driver.get("https://www.truecaller.com/")
sleep(3)

elem = driver.find_element_by_xpath("/html/body/div/div[4]/span/div/div[2]/button[1]")
elem.click()
# Login
elem0 = driver.find_element_by_xpath("/html/body/div/div[1]/nav/div[1]/a[1]")
elem0.click()
sleep(5)
# mircosoft account chose
elem1 = driver.find_element_by_xpath("/html/body/div/main/div/a[2]")
elem1.click()
sleep(4)
# user name
elem2 = driver.find_element_by_xpath("//*[@id='i0116']")
sleep(3)
elem2.send_keys(user)
# Login
elem3 = driver.find_element_by_xpath("//*[@id='idSIButton9']")
elem3.click()
# Password
sleep(5)
elem4 = driver.find_element_by_xpath("//*[@id='i0118']")
elem4.send_keys(password)
sleep(2)
# Login
elem5 = driver.find_element_by_xpath("//*[@id='idSIButton9']")
elem5.click()
sleep(8)

#Stay signed in
elem8 = driver.find_element_by_xpath("/html/body/div/form/div/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input")
elem8.click()
sleep(5)
#search number
elem6 = driver.find_element_by_xpath("/html/body/div/nav/div/form/input")
elem6.send_keys(num)
elem6.submit()
print('========================== ')
# Enter
sleep(5)
element1 = driver.find_element_by_xpath("/html/body/div/main/div/div[1]")
element_text3 = element1.text
element_attribute_value = element1.get_attribute('value')
print ('{0}'.format(element_text3))
print('========================== ')
driver.quit()
