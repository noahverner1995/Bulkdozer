# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 06:40:06 2022

@author: Noah
"""

import os
import pandas as pd
if os.name == 'nt': # Let's add some colors for the lulz
    from ctypes import windll
    k = windll.kernel32
    k.SetConsoleMode(k.GetStdHandle(-11), 7)
import pyautogui
import time
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

opt = Options() #the variable that will store the selenium options
opt.add_experimental_option("debuggerAddress", "localhost:9222") #this allows bulk-dozer to take control of your Chrome Browser in DevTools mode.

def wait_xpath(code): #function to wait for the element to be found by its XPATH
    WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.XPATH, code)))

def check_path(infile): #evaluate if the path provided actually exists in the os.
    return os.path.exists(infile) 

def containsNumber(value): #evaluate if a string contains a number
    for character in value:
        if character.isdigit():
            return True
    return False

def check_positive_float(potential_float): #evalute if a string can be converted to a positive float
    try:
        float(potential_float)
        if float(potential_float) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False

print('\033[0;37;44mHi Sailor! I am "Bulk-dozer", a bulk uploader built by @NoahVerner \033[0m')
print('\033[0;37;44m My aim is to bulk upload an NFT collection of yours to OpenSea =) \033[0m')
time.sleep(2)
print('')

print('\033[0;37;42mAllow me to show you the variables you are going to define:\033[0m')
time.sleep(2)
print('')

print('\033[0;37;35mItem Name (without any numbers nor hashtag (#), I will do that for you):\033[0m')
print('\033[0;37;35mExternal link (if desired):\033[0m')
print('\033[0;37;35mDescription:\033[0m')
print('\033[0;37;35mCollection Link:\033[0m')
print('\033[0;37;35mStart number:\033[0m')
print('\033[0;37;35mEnd number:\033[0m')
print('\033[0;37;35mPayment method (ETH, or DAI):\033[0m')
print('\033[0;37;35mInitial price:\033[0m')
print('\033[0;37;35mNFT Folder path:\033[0m')
print('\033[0;37;35mMetadata File path:\033[0m')
time.sleep(2)
print('')

print('\033[0;37;41mAlso, the following constants will be used by default in this automated process and cannot be changed:\033[0m')
time.sleep(2.7)
print('')

print('\033[0;37;43mBlockchain: Polygon (MATIC)\033[0m')
print('\033[0;37;43mDuration of individual listings: 6 months\033[0m')
print('\033[0;37;43mImage format: .PNG\033[0m')
time.sleep(1.9)
print('')


item_name = input('\033[0;37;32mAll right, let us start with the first one, define your Item Name:\033[0m ')
if containsNumber(item_name) == True or "#" in item_name:
    while True:
        item_name = input('\033[0;37;41mI told you that I will be adding the # and numbers! Try again, define your Item Name without "#" or numbers:\033[0m ')
        if containsNumber(item_name) == False and "#" not in item_name:
            break
external_link = input('\033[0;37;32mOkay, now tell me, do you want to add an external link? Type "y" if yes or "n" if not:\033[0m ')
while True:
    if external_link == 'y':
        external_link == input('\033[0;37;32mSure, paste here the link and press Enter:\033[0m ')              
        break
    elif external_link == 'n':
        external_link = None
        break
    elif external_link != 'y' or external_link != 'n':
        external_link= input("\033[0;37;41mInvalid Input, Type 'y' or 'n' without single quotation marks:\033[0m ")
description = input('\033[0;37;32mOkay,now paste here the description of your NFTs and press Enter:\033[0m ')
collection_link = input('\033[0;37;32mCool, now paste here the link of your collection and press Enter:\033[0m ')
while True:
    if 'https://opensea.io/collection/' in collection_link:
        break
    else:
        collection_link = input('\033[0;37;41mYou must paste a valid collection link from OpenSea! Try again, paste the RIGHT LINK OF YOUR NFT COLLECTION and press Enter:\033[0m')
start_number = input('\033[0;37;32mNice, now paste here the number of the first NFT you want to mint (DO NOT INCLUDE .PNG) and press Enter:\033[0m ')
while True: #here bulkd-dozer makes sure the user provide only integer numbers for the variables start_number and end_number 
    if start_number.isdigit() == True:            
        start_number = int(start_number)
        if start_number>= 0:                
            end_number = input('\033[0;37;32mNice, now paste here the number of the last NFT you want to mint (DO NOT INCLUDE .PNG) and press Enter:\033[0m ')
            while True:
                if end_number.isdigit() == True:
                    end_number = int(end_number)
                    if end_number > start_number:
                        break
                    elif end_number < start_number:
                        end_number = input('\033[0;37;41mWhy did you paste a number less than the initial one? try again with a greater one:\033[0m ')
                    elif end_number == start_number:
                        end_number = input('\033[0;37;41mWhy did you paste the same number? try again with a greater one:\033[0m ')
                else:
                    end_number = input('\033[0;37;41mI told you to paste only integer numbers equal or greater than 0! Try again, paste the number of your last NFT and press Enter:\033[0m ')   
            break
        else:
            start_number = input('\033[0;37;41mI told you to paste only integer numbers equal or greater than 0! Try again, paste the number of your first NFT and press Enter:\033[0m ')                                
    else:
        start_number = input('\033[0;37;41mI told you to paste only integer numbers equal or greater than 0! Try again, paste the number of your first NFT and press Enter:\033[0m ')
payment_method = input("\033[0;37;32mGreat, now define your desired payment method (Can only choose 'ETH' or 'DAI' without single quotation marks):\033[0m ")
while True: #here the bulk-dozer asks for the payment method and the initial price for the NFTs
    if payment_method == 'ETH':       
        initial_price = input("\033[0;37;32mFine, now define the initial price in ETH for your NFTs:\033[0m ")
        while True:
            if check_positive_float(initial_price) == True:
                initial_price = float(initial_price)
                break
            else:
                initial_price = input('\033[0;37;41mYou must paste only decimal numbers (float) equal or greater than 0! Try again, paste the initial price in ETH for bnyour NFTs and press Enter:\033[0m ')                  
        break
    elif payment_method == 'DAI':
        initial_price = input("\033[0;37;32mFine, now define the initial price in DAI for your NFTs:\033[0m ")
        while True:
            if check_positive_float(initial_price) == True:
                initial_price = float(initial_price)
                break
            else:
                initial_price = input('\033[0;37;41mYou must paste only decimal numbers (float) equal or greater than 0! Try again, paste the initial price in DAI for your NFTs and press Enter:\033[0m ')                  
        break
    elif payment_method != 'ETH' or payment_method != 'DAI':
        payment_method= input("\033[0;37;41mInvalid Input, Type only 'ETH' or 'DAI' without single quotation marks:\033[0m ")         
nft_folder_path = input("\033[0;37;32mWe are almost done! Now, define the path at which your NFTs are located:\033[0m ")
unfound_images = 0
while True:   
    if check_path(nft_folder_path) == False:
        print('\033[31;1;4mThis PATH is invalid!\033[0m')
        nft_folder_path = input('Please type the RIGHT NFT FOLDER PATH:')
    elif check_path(nft_folder_path) == True:
        while start_number <= end_number:
            image_path_checker = nft_folder_path+'\\'+str(start_number)+'.png'
            if check_path(image_path_checker) == False:
                print(f'the file {start_number}.png does not exist at the path provided')
                unfound_images += 1
            start_number += 1
        if unfound_images == 0:
            break            
        elif unfound_images > 0:
            print('\033[0;37;41mThere are some files missing, see above, recover them and save it in the previous path or give me another path that has those files:\033[0m ')
            unfound_images = 0
            nft_folder_path = input('\033[0;37;32mNow, define the right path at which your images are located :\033[0m ')
metadata_file_path = input("\033[0;37;32mHere's the last one! Define the path at which your NFT Metadata is located:\033[0m ")
while True:
    if check_path(metadata_file_path) == False:
        print('\033[31;1;4mThis PATH is invalid!\033[0m')
        metadata_file_path = input('Please type the RIGHT NFT METADATA FILE PATH:')
    elif check_path(metadata_file_path) == True:
        if metadata_file_path.endswith('.csv'): #verify the path provided includes the csv file that has the metadata of NFTs
            break
        else:
            metadata_file_path = input('\033[0;37;41mThe path provided did not contain the .csv file with the metadata, make sure you know the RIGHT NFT METADATA FILE PATH and paste it here again:\033[0m ')
print('\033[0;37;42mAll right, let me show you how you defined the variables for this collection:\033[0m')
time.sleep(2)
print('')

print(f'\033[0;37;35mItem Name:\033[0m {item_name}')
print(f'\033[0;37;35mExternal link\033[0m {external_link}')
print(f'\033[0;37;35mDescription:\033[0m {description}')
print(f'\033[0;37;35mCollection Name:\033[0m {collection_link}')
print(f'\033[0;37;35mStart number:\033[0m {start_number}')
print(f'\033[0;37;35mEnd number:\033[0m {end_number}')
print(f'\033[0;37;35mPayment method:\033[0m {payment_method}')
print(f'\033[0;37;35mInitial price:\033[0m {initial_price}')
print(f'\033[0;37;35mNFT Folder path:\033[0m {nft_folder_path}')
print(f'\033[0;37;35mMetadata File path:\033[0m {metadata_file_path}')
time.sleep(2.5)
print('')

chrome_driver_path = input('Okay, now type YOUR chrome driver path (include chromedriver.exe): ') #ask the user for the path at which cromedriver.exe is located   
while True:
    if check_path(chrome_driver_path) == False:
        print('\033[31;1;4mThis PATH is invalid!\033[0m')
        chrome_driver_path = input('Please type the RIGHT CHROME DRIVER PATH:')
    elif check_path(chrome_driver_path) == True:
        if chrome_driver_path.endswith('chromedriver.exe'):
            s = Service(fr'{chrome_driver_path}') #Use the chrome driver located at the corresponding path
            break
        else:
            chrome_driver_path = input('\033[33;1;4mThe path provided does not seem to be the right one, try again:\033[0m ')
driver = webdriver.Chrome(service=s, options=opt) #execute the chromedriver.exe with the previous conditions
print('\033[0;37;44mThe bulk uploading of your NFTs to OpenSea will start soon.\033[0m')
time.sleep(1.2)
print('\033[0;37;44mOnce started do not interfere with this process until it has been finished.\033[0m')

time.sleep(1.7)

nft_counter = start_number #counter for the while loop
while nft_counter <= end_number:
    if driver.current_url == collection_link:
        if nft_counter == start_number:
            print(f'\033[0;37;44mStarting minting the nft #{start_number}, the final nft to be minted is #{end_number}\033[0m')
        elif nft_counter > start_number:
            print(f'\033[0;37;44mMinting #{nft_counter}\033[0m')
        while True: #a simple trick to counter possible 504 errors and related scenarios
            try:
                wait_xpath('//*[@id="main"]/div/div/section/div/form/div[1]/div/div[2]') #wait for the _imageUpload button to be present and located
                checker_imageupload = np.size(driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/section/div/form/div[1]/div/div[2]'))
                if checker_imageupload == 1:
                    break
            except TimeoutException:
                print('I ended up getting a TimeOutException while waiting for the image upload element to be present within the page')
                print('I am going to reload the page to see if this solves the issue')
                driver.refresh()
        time.sleep(1.3)
        nft_to_be_selected = nft_folder_path+"\\"+str(nft_counter)+".png"
        imageUpload = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div/form/div[1]/div/div[2]').click() #click on the upload image button
        time.sleep(1.5) #wait for the dialog to load
        pyautogui.write(nft_to_be_selected) #this imitates human behaviour, the blink text cursor must be within the 'Name' textbox from the Open dialog
        pyautogui.press('enter', presses = 2) #paste the path of the current NFT and then press Enter
        textbox_item_name = driver.find_element(By.XPATH, '//*[@id="name"]').send_keys(item_name+" "+"#"+str(nft_counter)) #paste the item_name info
        if external_link != None:
            textbox_external_link = driver.find_element(By.XPATH, '//*[@id="external_link"]').send_keys(external_link) #paste the external_link info if it's different than None
        driver.execute_script("window.scrollBy(0,690)", "") #scroll down the page to know what's being added, right at the textbox_description's height
        textbox_description = driver.find_element(By.XPATH, '//*[@id="description"]').send_keys(description) #paste the description info
        df_metadata = pd.read_csv(metadata_file_path, index_col=0) #import the metadata_file_path
        df_metadata.columns = df_metadata.columns.str.split('.').str[0].astype(int) #make sure that the names of the paired columns stay integers
        row = nft_counter #assign the current nft_counter to the row variable that will be used to get the corresponding metadata_row
        s = df_metadata.iloc[row] #get only the corresponding metadata row for the current NFT
        current_dictionary = dict(zip(s[~s.index.duplicated()], s[~s.index.duplicated(keep='last')])) #convert the metadata_row to a dictionary for later use
        print('Metadata to add:')
        print(f'{current_dictionary}')
        button_plus_properties = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div[2]/form/section/div[1]/div/div[2]/button').click() #click on the "+" button of Properties
        wait_xpath('/html/body/div/div/div/div/section/button') #wait for button_add_more to be loaded and located
        type_array = list(current_dictionary.keys()) #get the keys which will be send as types
        name_array = list(current_dictionary.values()) #get the values which will be send as values 
        i = 1
        button_add_more = driver.find_element(By.XPATH, '/html/body/div/div/div/div/section/button').click() #add a new textbox type and textbox value
        while i <= len(current_dictionary): #iterate over the types and values lulz
            xpath_type = f'/html/body/div/div/div/div/section/table/tbody/tr[{i}]/td[1]/div/div/input' #xpath of the i type
            xpath_name = f'/html/body/div/div/div/div/section/table/tbody/tr[{i}]/td[2]/div/div/input' #xpath of the i value
            time.sleep(0.25)
            button_xpath_type = driver.find_element(By.XPATH, xpath_type).send_keys(type_array[i-1]) #find the ith textbox type and paste the ith-1 element from the type_array variable
            time.sleep(0.25)
            button_xpath_name = driver.find_element(By.XPATH, xpath_name).send_keys(name_array[i-1]) #find the ith textbox value and paste the ith-1 element from the name_array variable 
            if i != (len(current_dictionary)-1): #as long as i is not equal to the lenght of the current_dictionary
                button_add_more = driver.find_element(By.XPATH, '/html/body/div/div/div/div/section/button').click() #add a new textbox type and textbox value
            i +=1 
        button_save_metadata = driver.find_element(By.XPATH, '/html/body/div/div/div/div/footer/button') #find the save button in this dialog
        button_save_metadata.click() #save the metadata
        time.sleep(0.5)
        driver.execute_script("window.scrollBy(0,890)", "") #scroll down the page to know what's being added, right at the Blockchain's height
        blockchain_checker = driver.find_element(By.XPATH, '//*[@id="chain"]').get_attribute('value') #store the current Blockchain to be used
        if blockchain_checker != 'Polygon': #verify if it WAS NOT set to Polygon
            button_blockchain = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div[2]/form/div[7]/div/div[2]').click() #deploy other blockchain options
            button_polygon = driver.find_element(By.XPATH, '//*[@id="tippy-88"]/div/div/div/ul/li/button') #find the polygon one
            button_polygon.click() #choose it
        time.sleep(1)    
        button_create = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div[2]/form/div[9]/div[1]/span/button').click() #create the NFT (Metadata NOT FROZEN)
        while True: #let the page stop buffering and wait for the new page even if it then throws 504 errors or related scenarios
            try:
                WebDriverWait(driver, 1.5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/div/div/section/div[2]/form/div[9]/div[1]/span/button'))) #wait for the button_create to be present and located
            except TimeoutException:
                print('success')
                break
        number_of_tries = 0
        while True: #a simple trick to counter possible 504 errors and related scenarios
            if number_of_tries == 0:
                try:
                    wait_xpath('/html/body/div[5]/div/div/div/div[1]/header') #wait for the header that notifies the user that the NFT has been created
                    checker_button_close_header = np.size(driver.find_elements(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button'))
                    if checker_button_close_header == 1:
                        button_close_header_nft_created = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[2]/button').click() #close this header
                        wait_xpath('//*[@id="main"]/div/div/div[1]/div/span[2]/a') #wait for the button_sell to be located
                        break
                except TimeoutException:
                    print('I ended up getting a TimeOutException while waiting for the button for closing the header to be present within the page')
                    print('I am going to reload the page to see if this solves the issue')
                    number_of_tries += 1
                    driver.refresh()
            else:
                try:
                    wait_xpath('//*[@id="main"]/div/div/div[1]/div/span[2]/a') #wait for the button_sell to be located
                    checker_sell_button = np.size(driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/span[2]/a'))
                    if checker_sell_button == 1:
                        break
                except TimeoutException:
                    print('Did not work, I am going to refresh again')
                    number_of_tries += 1
                    driver.refresh()        
        time.sleep(1)
        url_of_nft_recently_minted = driver.current_url #get the current url of the nft that was minted moments ago
        properties_found = np.size(driver.find_elements(By.XPATH, '//*[text()="Properties"]')) #store the amount of web elements that display the text "Properties"
        while True:
            if properties_found == 0: #evalaute if the nft that was minted moments ago DID NOT STORE THE METADATA
                button_edit = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[1]/div/span/a')
                button_edit.click()
                wait_xpath('//*[@id="main"]/div/div/section/div/form/div[1]/div/div[2]') #wait for the _imageUpload button to be present and located
                driver.execute_script("window.scrollBy(0,890)", "") #scroll down the page to know what's being added, right at the Blockchain's height
                number_of_properties = np.size(driver.find_elements(By.XPATH, '/html/body/div[1]/div/main/div/div/section/div[2]/form/section/div[1]/div[2]/a')) #check if there are properties already
                if number_of_properties > 0:
                    driver.get(url_of_nft_recently_minted)
                    while True: #a simple trick to counter possible 504 errors and related scenarios
                        try:
                            wait_xpath('//*[@id="main"]/div/div/div[1]/div/span[2]/a') #wait for the button_sell to be located
                            checker_sell_button = np.size(driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/span[2]/a'))
                            if checker_sell_button == 1:
                                break
                        except TimeoutException:
                            print('I ended up getting a TimeOutException while waiting for the button for selling to be present within the page')
                            print('I am going to reload the page to see if this solves the issue')
                            driver.refresh()
                    time.sleep(0.5)
                    properties_found = np.size(driver.find_elements(By.XPATH, '//*[text()="Properties"]')) #store the amount of web elements that display the text "Properties"
                    if properties_found == 1:
                        break
                elif number_of_properties == 0:
                    button_plus_properties = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/section/div[2]/form/section/div[1]/div/div[2]/button').click() #click on the "+" button of Properties
                    wait_xpath('/html/body/div/div/div/div/section/button') #wait for button_add_more to be loaded and located
                    button_add_more = driver.find_element(By.XPATH, '/html/body/div/div/div/div/section/button').click() #add a new textbox type and textbox value
                    i = 1
                    while i <= len(current_dictionary): #iterate over the types and values lulz
                        xpath_type = f'/html/body/div/div/div/div/section/table/tbody/tr[{i}]/td[1]/div/div/input' #xpath of the i type
                        xpath_name = f'/html/body/div/div/div/div/section/table/tbody/tr[{i}]/td[2]/div/div/input' #xpath of the i value
                        time.sleep(0.25)
                        button_xpath_type = driver.find_element(By.XPATH, xpath_type).send_keys(type_array[i-1]) #find the ith textbox type and paste the ith-1 element from the type_array variable
                        time.sleep(0.25)
                        button_xpath_name = driver.find_element(By.XPATH, xpath_name).send_keys(name_array[i-1]) #find the ith textbox value and paste the ith-1 element from the name_array variable 
                        if i != (len(current_dictionary)-1): #as long as i is not equal to the lenght of the current_dictionary
                            button_add_more = driver.find_element(By.XPATH, '/html/body/div/div/div/div/section/button').click() #add a new textbox type and textbox value
                        i +=1
                    button_save_metadata = driver.find_element(By.XPATH, '/html/body/div/div/div/div/footer/button') #find the save button in this dialog
                    button_save_metadata.click() #save the metadata
                    time.sleep(0.5)
                    button_save_changes = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/section/div[2]/form/div[8]/div[1]/span/button')
                    button_save_changes.click()
                    wait_xpath('//*[text()="Success!"]')
                    driver.get(url_of_nft_recently_minted)      
                    while True: #a simple trick to counter possible 504 errors and related scenarios
                        try:
                            wait_xpath('//*[@id="main"]/div/div/div[1]/div/span[2]/a') #wait for the button_sell to be located
                            checker_sell_button = np.size(driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/span[2]/a'))
                            if checker_sell_button == 1:
                                break
                        except TimeoutException:
                            driver.refresh()
                    time.sleep(0.7)
                    properties_found = np.size(driver.find_elements(By.XPATH, '//*[text()="Properties"]')) #store the amount of web elements that display the text "Properties"
            else: #if the nft that was minted moments ago DID STORE THE METADATA, break the loop
                break   
        button_sell = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[1]/div/span[2]/a') #find the sell button
        time.sleep(1)
        button_sell.click()
        while True: #a simple trick to counter possible 504 errors and related scenarios
            try:
                wait_xpath('//*[@id="main"]/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[2]') #wait for the amount textbox to be present
                checker_amount_textbox = np.size(driver.find_elements(By.XPATH, '//*[@id="main"]/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[2]'))
                if checker_amount_textbox == 1:
                    break
            except TimeoutException:
                print('I ended up getting a TimeOutException while waiting for the amount textbox within the page')
                print('I am going to reload the page to see if this solves the issue')
                driver.refresh()                
        payment_method_checker = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[1]/input').get_attribute('value')
        if payment_method_checker != payment_method:
            button_payment_method = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[1]')
            button_payment_method.click()
            wait_xpath('/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[3]/div/div/div/ul') #wait for the options div to be fully present
            button_dai = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[3]/div/div/div/ul/li[1]/button')
            button_dai.click()
        textbox_price_amount = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[1]/div/div[2]/div/div/div[2]/input').send_keys(str(initial_price)) #paste the iniitial_price
        button_duration = driver.find_element(By.CSS_SELECTOR, '#duration')
        button_duration.click()
        max_date_ending = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/input').get_attribute('max')
        current_date_ending = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/input').get_attribute('value')
        array_max_date_ending = max_date_ending.split('-')
        array_current_date_ending = current_date_ending.split('-')
        button_ending = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/input')
        button_ending.click()
        while True:
            if int(array_current_date_ending[2]) <= 28:
                counter = 0
                textbox_ending = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/input').click() #Click the ending textbox
                pyautogui.press('right')
                while counter < 5:
                    pyautogui.press('up')
                    counter += 1
                counter = 0
                current_date_ending = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/input').get_attribute('value')
                array_current_date_ending = current_date_ending.split('-')
                if int(array_current_date_ending[2]) < int(array_max_date_ending[2]):
                    pyautogui.press('left')
                    number_of_presses = int(array_max_date_ending[2]) - int(array_current_date_ending[2])
                    while counter != number_of_presses:
                        pyautogui.press('up')
                        counter += 1
                    pyautogui.press('enter')
                    break
                elif int(array_current_date_ending[2]) == int(array_max_date_ending[2]):
                    pyautogui.press('enter')
                    break
            else:
                counter = 0
                textbox_ending = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/input').click() #Click the ending textbox
                number_of_presses = int(array_current_date_ending[2]) - 28
                while counter != number_of_presses:
                    pyautogui.press('down')
                    counter += 1
                pyautogui.press('right')
                while counter < 5:
                    pyautogui.press('up')
                    counter += 1
                counter = 0
                current_date_ending = driver.find_element(By.XPATH, '/html/body/div[1]/div/main/div/div/div[3]/div/div[2]/div/div[1]/form/div[2]/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/input').get_attribute('value')
                array_current_date_ending = current_date_ending.split('-')
                if int(array_current_date_ending[2]) < int(array_max_date_ending[2]):
                    pyautogui.press('left')
                    number_of_presses = int(array_max_date_ending[2]) - int(array_current_date_ending[2])
                    while counter != number_of_presses:
                        pyautogui.press('up')
                        counter += 1
                    pyautogui.press('enter')
                    break
                elif int(array_current_date_ending[2]) == int(array_max_date_ending[2]):
                    pyautogui.press('enter')
                    break
        main_page = driver.current_window_handle #get the current url 
        button_complete_listing = driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div[3]/div/div[2]/div/div[1]/form/div[5]/button')
        button_complete_listing.click()
        wait_xpath('//*[text()="Sign"]') #wait for the "Sign" button to appear
        button_sign = driver.find_element(By.XPATH, '//*[text()="Sign"]') #find the "Sign" button
        button_sign.click()
        time.sleep(1.5)
        for handle in driver.window_handles:
            if handle != main_page:
                login_page = handle
        driver.switch_to.window(login_page) # change the control to Metamask window for authorizing the selling of your NFT
        wait_xpath('/html/body/div[1]/div/div[2]/div/div[3]/button[2]')
        button_sign_metamask = driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div[3]/button[2]')
        button_sign_metamask.click()
        time.sleep(1.5)
        driver.switch_to.window(main_page) #go back to the main_page
        wait_xpath('//*[text()="close"]') #wait for the "X" button to close the dialog
        button_close_nft_listed_dialog = driver.find_element(By.XPATH, '//*[text()="close"]')
        button_close_nft_listed_dialog.click()
        driver.get(url_of_nft_recently_minted)
        while True: #a simple trick to counter possible 504 errors and related scenarios
            try:
                wait_xpath('/html/body/div[1]/div/main/div/div/div[2]/div[1]/div/div[1]/div[2]/section[1]/div/div[1]/div/a') #wait for the link of the collection to be located in the new page
                checker_collection_link = np.size(driver.find_elements(By.XPATH, '/html/body/div[1]/div/main/div/div/div[2]/div[1]/div/div[1]/div[2]/section[1]/div/div[1]/div/a'))
                if checker_collection_link == 1:
                    break
            except TimeoutException:
                print('I ended up getting a TimeOutException while waiting for the collection link within the page')
                print('I am going to reload the page to see if this solves the issue')
                driver.refresh() 
        time.sleep(1.3)
        nft_counter += 1        
    else:
        driver.get(collection_link)
        while True: #a simple trick to counter possible 504 errors and related scenarios
            try:
                wait_xpath('//*[@id="__next"]/div[1]/main/div/div/div[1]/span/a') #wait for the button_add_item to be present and located
                checker_add_item_button = np.size(driver.find_elements(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div[1]/span/a'))
                if checker_add_item_button == 1:
                    break            
            except TimeoutException:
                print('I ended up getting a TimeOutException while waiting for the add item button within the page')
                print('I am going to reload the page to see if this solves the issue')
        button_add_item = driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/main/div/div/div[1]/span/a').click() #by doing this, the new link will automatically set the corresponding collection as default