"""


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!This is just a worksheet!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




Instructions:
•	Go to https://www.abcmouse.com
•	Click “Sign Up” button
•	Verify that  https://www.abcmouse.com/abt/register page is returned
•	Enter Email address (any email address)
•	Click “Submit” button
•	Verify that https://www.abcmouse.com/abt/subscription page is returned.
•	Verify that on subscription page, “Become a Member!” text is rendered.

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from configparser import ConfigParser

#Read config.ini file
config_object = ConfigParser()
config_object.read("config.ini")



def expand_shadow_element(element):
  shadow_root = browser.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

def validateURL(expectedVal):
  currURL=browser.current_url
  if currURL==expectedVal:
    return ("URL is verified")
  else:
    return ("URL is not same as expected")

browser = webdriver.Chrome()
browser.get("https://www.abcmouse.com")
browser.maximize_window()

browser.implicitly_wait(10)
"""
Signup Button
document.querySelector("route-view").shadowRoot.querySelector("home-element").shadowRoot.querySelector("main-layout > home-header >authstate-context:nth-child(3) > signup-button")
"""


root1 = browser.find_element(By.TAG_NAME,"route-view")
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element(By.CSS_SELECTOR,"home-element")
shadow_root2 = expand_shadow_element(root2)

signupBtn = shadow_root2.find_element(By.CSS_SELECTOR,"main-layout > home-header >authstate-context:nth-child(3) > signup-button")


signupBtn.click()

browser.implicitly_wait(10)
## Verifying URL returned is correct


expectedURL=emailinfo = config_object["testData"]["url1"]
print(validateURL(expectedURL))
##assert expectedURL == actualURL########################################

### enter email

"""
Email Text Box
document.querySelector("route-view").shadowRoot.querySelector("prospect-register-page").
shadowRoot.querySelector("main-layout > main > div:nth-child(3)> div> div:nth-child(3) > form> div> div> input")
"""


root1 = browser.find_element(By.TAG_NAME,"route-view")
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element(By.CSS_SELECTOR,"prospect-register-page")
shadow_root2 = expand_shadow_element(root2)

emailBox = shadow_root2.find_element(By.CSS_SELECTOR,"main-layout > main > div:nth-child(3)> div> div:nth-child(3) > form> div> div> input")

#Get the password
emailinfo = config_object["testData"]["email"]

emailBox.send_keys(emailinfo)

"""
submit Button:
document.querySelector("route-view").shadowRoot.querySelector("prospect-register-page").
shadowRoot.querySelector("main-layout > main > div:nth-child(3)> div> div:nth-child(3) > form > div:nth-child(3) > button")
"""
root1 = browser.find_element(By.TAG_NAME,"route-view")
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element(By.CSS_SELECTOR,"prospect-register-page")
shadow_root2 = expand_shadow_element(root2)

submitButton = shadow_root2.find_element(By.CSS_SELECTOR,"main-layout > main > div:nth-child(3)> div> div:nth-child(3) > form > div:nth-child(3) > button")
submitButton.click()

browser.implicitly_wait(10)

#Verifying URL


signupURL=emailinfo = config_object["testData"]["url2"]
print(validateURL((signupURL)))
#assert signUpURL in URL ######################################


##verifying //

""" 
Page Label
document.querySelector("route-view").shadowRoot.querySelector("subscription-page").
shadowRoot.querySelector("main-layout > main >h1")
"""

##accessing the shadow root
root1 = browser.find_element(By.TAG_NAME,'route-view')
shadow_root1 = expand_shadow_element(root1)

root2 = shadow_root1.find_element(By.CSS_SELECTOR,'subscription-page')
shadow_root2 = expand_shadow_element(root2)

actualPageTag = shadow_root2.find_element(By.CSS_SELECTOR,"main-layout > main >h1")

expectedPageTag="Become a Member!"
assert actualPageTag.text==expectedPageTag

browser.close()
