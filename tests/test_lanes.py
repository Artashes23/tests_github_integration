from pages.lanes import check_initiative_lanes
import dotenv
from dotenv import load_dotenv
import os
from simple_settings import settings

class Test_Lanes(check_initiative_lanes):
    load_dotenv()
    def test_check_status_updates(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('PROD_URL'))
        self.check_lane_updates()

    
        

    
    