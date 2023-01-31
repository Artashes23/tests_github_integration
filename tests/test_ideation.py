from .pages.create_ideation import Check_Ideations
from dotenv import load_dotenv
import os



class Test_Ideations(Check_Ideations):
    load_dotenv
    def test_create_delete_ideations(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('Prod_Url'))
        self.check_create_delete()
