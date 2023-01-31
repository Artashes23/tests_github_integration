from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class BasePage():

    def find_text_multiple(self,by_locator):
        a = WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located(by_locator))
        return a.text

    def find_multiple_elements(self,by_locator):
        a = WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located(by_locator))
        return a

    def browsers(self,setup):
        self.browser = setup
        

    def count_elements(self,by_locator):
        all_elements = WebDriverWait(self.browser,10).until(EC.presence_of_all_elements_located(by_locator))
        return len(all_elements)
        
    
    def text_assertion(self,By_locator,text):
        WebDriverWait(self.browser,10).until(EC.text_to_be_present_in_element(By_locator,text))
        return True
        

    def click(self,by_locator):
        try:
        
            WebDriverWait(self.browser,40).until((EC.presence_of_element_located(by_locator))).click()
        except:
            WebDriverWait(self.browser,40).until((EC.visibility_of_element_located(by_locator))).click()
    
    def send_keys(self,by_locator,text_):
        WebDriverWait(self.browser,20).until(EC.presence_of_element_located(by_locator)).send_keys(text_)

    def validation_message(self,by_locator,message_types):
        message = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable(by_locator)).get_attribute(message_types)
        return message
    
    def save_screenshot(self,by_locator,file_name):
        WebDriverWait(self.browser,10).until(EC.visibility_of_element_located(by_locator)).screenshot(file_name)
    
    def clear(self,by_locator):
        WebDriverWait(self.browser,10).until(EC.presence_of_element_located(by_locator)).clear()
    
    def find_text(self,by_locator):
        WebDriverWait(self.browser,10).until((EC.visibility_of_element_located(by_locator))).getText()

    def find_text(self,by_locator):
        a = WebDriverWait(self.browser,20).until((EC.visibility_of_element_located(by_locator)))
        return a.text
        

    def select(self,by_locator,visible_text):
        WebDriverWait(self.browser,10).until((EC.visibility_of_element_located(by_locator))).select_by_visible_text(visible_text)

    def get_url_after_switching(self,desired_num):
        self.browser.switch_to.window(self.browser.window_handles[desired_num])
        return  self.browser.current_url

    def switch_windows(self,desired_num):
        self.browser.switch_to.window(self.browser.window_handles[desired_num])

    def get_current_url(self,str):
        WebDriverWait(self.browser,10).until((EC.url_contains(str)))

    def element_presence(self,by_locator):
        WebDriverWait(self.browser,10).until(EC.presence_of_element_located(by_locator))
        return True

    def get_current_url(self):
        return self.browser.current_url

   


    
    
    def checkbox_is_selected(self,by_locator):
        elem = WebDriverWait(self.browser,25).until(EC.presence_of_element_located(by_locator))
        return elem.is_selected()
