from ..pages.lanes import check_initiative_lanes
import os


class Test_Lanes(check_initiative_lanes):
    
    def test_check_status_updates(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('PROD_URL'))
        self.check_lane_updates()

    
        

    
    
