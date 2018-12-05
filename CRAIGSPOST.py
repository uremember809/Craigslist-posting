# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:36:48 2017

@author: matt
"""


from selenium import webdriver
import mattemail, time

card = 'cardNumber'
cvn = 'cvNumber'
month = 'expMonth'
year = 'expYear'
first = 'cardFirstName'
last = 'cardLastName'
addr = 'cardAddress'
city = 'cardCity'
state = 'cardState'
zipcode = 'cardPostal'
contact = 'contactName'
phone = 'contactPhone'
email = 'contactEmail'





info = {card:'4695965088888888', cvn:'888', month:'10', year:'2022', first:'My', last:'Name', addr:'3400 My Home Dr', city:'Hometown', state:'HO', zipcode:'12345', contact:'My Name', phone:'3478888888', email:''}


browser = webdriver.Chrome()
browser.get('http://craigslist.com')

try:
    elem = browser.find_element_by_link_text('my account')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')
    
elem.click()


#login
emailElem = browser.find_element_by_id('inputEmailHandle')
emailElem.send_keys('eevoony@gmail.com')
pswd = browser.find_element_by_id('inputPassword')
pswd.send_keys('29827cyqP)')
pswd.submit()


  
    
if browser.find_elements_by_name('go'):
        
    #click repost
    repost = browser.find_elements_by_name('go')
    repost[2].click()
    
    
    #confirm repost
    repostagain = browser.find_elements_by_class_name('managebtn')
    repostagain[1].click()
    
    #Publish Button
    publish = browser.find_element_by_class_name('button')
    publish.click()
    
    
    #Continue
    continuebutton = browser.find_element_by_tag_name('button')
    continuebutton.click()
    
    
    #card info
    #card = browser.find_element_by_name('cardNumber')
    #card.send_keys('5425448332323236')
    #
    #cvn = browser.find_element_by_name('cvNumber')
    #cvn.send_keys('362')
    #
    #month = browser.find_element_by_name('expMonth')
    #month.send_keys('09')
    #
    #year = browser.find_element_by_name('expYear')
    #year.send_keys('2021')
    #
    #first = browser.find_element_by_name('cardFirstName')
    #first.send_keys('Yongqing')
    #
    #last = browser.find_element_by_name('cardLastName')
    #last.send_keys('Cao')
    #
    #addr = browser.find_element_by_name('cardAddress')
    #addr.send_keys('3400 Cherry Hill Dr')
    #
    #city = browser.find_element_by_name('cardCity')
    #city.send_keys('Fairfield')
    #
    #state = browser.find_element_by_name('cardState')
    #state.send_keys('OH')
    #
    #zipcode = browser.find_element_by_name('cardPostal')
    #zipcode.send_keys('45014')
    #
    #contact = browser.find_element_by_name('contactName')
    #contact.send_keys('Matt Cao')
    #
    #phone = browser.find_element_by_name('contactPhone')
    #phone.send_keys('5138991888')
    #
    #email = browser.find_element_by_name('contactEmail')
    #email.send_keys('')
    
    for i in info:
        print(i)
        x = browser.find_element_by_name(i)
        x.send_keys(info[i])
    
    #submit
    finish = browser.find_element_by_name('finishForm')
    finish.submit()
    time.sleep(300)

elif browser.find_element_by_class_name('login-page-boxes'):
    
    
    from twilio.rest import Client
    # Your Account SID from twilio.com/console
    account_sid = "AC8c18f7dc3ec565711d4a06407660c662"
    # Your Auth Token from twilio.com/console
    auth_token  = "2b623ce4803b1f7e9ef2c05d717f414c"
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
            to="+15138960867", 
            from_="+15138472112",
            body="CAPTCHA, CAPTCHA, MANUAL")
    print(message.sid)
    
    
    import smtplib
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(' eevoony@gmail.com ', ' 29827cyq1414 ')
    smtpObj.sendmail(' eevoony@gmail.com ', ' eevoony@gmail.com ','Subject: Renew Failed\nMatt\n renew failed, manual please\n\nMatt')
    smtpObj.quit()
    
    mattemail.email('eevoony@gmail.com', 'Failed' , 'Hi, Matt')



else:
    
    from twilio.rest import Client
    # Your Account SID from twilio.com/console
    account_sid = "AC8c18f7dc3ec565711d4a06407660c662"
    # Your Auth Token from twilio.com/console
    auth_token  = "2b623ce4803b1f7e9ef2c05d717f414c"
    
    client = Client(account_sid, auth_token)
    
    message = client.messages.create(
            to="+15138960867", 
            from_="+15138472112",
            body="wrong, wrong, MANUAL")
    print(message.sid)
    
browser.close()
