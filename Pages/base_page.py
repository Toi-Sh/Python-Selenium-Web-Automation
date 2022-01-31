
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as W

class BasePage():
    title="ABCMouse"
    wait_time_out=5

    def __init__(self,drv):
        self.drv=drv
        self.wait_variable = W(self.drv,self.wait_time_out)

    def expand_shadow_element(self, element):
        shadow_root = self.drv.execute_script('return arguments[0].shadowRoot', element)
        return shadow_root
    def validateURL(self,expectedVal):
        currURL=self.drv.current_url
        try:
            assert currURL==expectedVal
            print("URL validation succesful")
        except:
            print("Assert Failed {} expected, actual {}".format(expectedVal, currURL))

    def click_signup_button(self):
        """
        Signup Button Query
        document.querySelector("route-view").shadowRoot.querySelector("home-element").shadowRoot.querySelector("main-layout > home-header >authstate-context:nth-child(3) > signup-button")
        """

        root1 = self.drv.find_element(By.TAG_NAME,"route-view")
        shadow_root1 = self.expand_shadow_element(root1)

        root2 = shadow_root1.find_element(By.CSS_SELECTOR,"home-element")
        shadow_root2 = self.expand_shadow_element(root2)

        signupBtn = shadow_root2.find_element(By.CSS_SELECTOR,"main-layout > home-header >authstate-context:nth-child(3) > signup-button")

        signupBtn.click()

        self.drv.implicitly_wait(5)
