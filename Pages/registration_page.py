from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W
from configparser import ConfigParser
#Read config.ini file
config_object = ConfigParser()

config_object.read("C:/Users/User/Documents/AgeOfLearning/config.ini")
emailinfo = config_object["testData"]["email"]
expectedPageTag= config_object["testData"]["pageTag"]


class RegistrationPage():
    wait_time_out=5
    def __init__(self,drv):
        self.drv=drv
        self.wait_variable = W(self.drv,self.wait_time_out)

    def expand_shadow_element(self, element):
        shadow_root = self.drv.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root

    def validateURL(self,expectedVal):
        currURL=self.drv.current_url
        # if currURL==expectedVal:
        #     return ("URL is verified")
        # else:
        #     return ("URL is not same as expected")
        try:
            assert currURL==expectedVal
            print("URL validation succesful")
        except:
            print("Assert Failed {} expected, actual {}".format(expectedVal, currURL))

    def enter_email_info(self):
        """
        Email Text Box Query
        document.querySelector("route-view").shadowRoot.querySelector("prospect-register-page").
        shadowRoot.querySelector("main-layout > main > div:nth-child(3)> div> div:nth-child(3) > form> div> div> input")
        """
        root1 = self.drv.find_element(By.TAG_NAME,"route-view")
        shadow_root1 = self.expand_shadow_element(root1)

        root2 = shadow_root1.find_element(By.CSS_SELECTOR,"prospect-register-page")
        shadow_root2 = self.expand_shadow_element(root2)

        emailBox = shadow_root2.find_element(By.CSS_SELECTOR,"main-layout > main > div:nth-child(3)> div> div:nth-child(3) > form> div> div> input")

        #Get the password


        emailBox.send_keys(emailinfo)

    def click_submit_button(self):
        """
        submit Button Query:
        document.querySelector("route-view").shadowRoot.querySelector("prospect-register-page").
        shadowRoot.querySelector("main-layout > main > div:nth-child(3)> div> div:nth-child(3) > form > div:nth-child(3) > button")
        """
        root1 = self.drv.find_element(By.TAG_NAME,"route-view")
        shadow_root1 = self.expand_shadow_element(root1)

        root2 = shadow_root1.find_element(By.CSS_SELECTOR,"prospect-register-page")
        shadow_root2 = self.expand_shadow_element(root2)

        submitButton = shadow_root2.find_element(By.CSS_SELECTOR,"main-layout > main > div:nth-child(3)> div> div:nth-child(3) > form > div:nth-child(3) > button")
        submitButton.click()
        print("Submit Button clicked")
        self.drv.implicitly_wait(5)

    def assert_page_tag(self):
        """
        Page Tag Qeury:
        document.querySelector("route-view").shadowRoot.querySelector("subscription-page").
        shadowRoot.querySelector("main-layout > main >h1")
        """
        root1 = self.drv.find_element(By.TAG_NAME,'route-view')
        shadow_root1 = self.expand_shadow_element(root1)

        root2 = shadow_root1.find_element(By.CSS_SELECTOR,'subscription-page')
        shadow_root2 = self.expand_shadow_element(root2)

        actualPageTag = shadow_root2.find_element(By.CSS_SELECTOR,"main-layout > main >h1")
        try:
            assert actualPageTag.text==expectedPageTag
            print("Page tag validation succesful")
        except:
            print("Assert Failed {} expected, actual {}".format(expectedPageTag, actualPageTag.text))
