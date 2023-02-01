from ..pages.settings import check_settings_page
import os

class Test_Settings(check_settings_page):
    load_dotenv
    def test_goal_add_delete(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('PROD_URL'))
        self.check_settings_add_delete_goal()

    
        


    
