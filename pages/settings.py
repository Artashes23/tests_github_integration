from ..pages.base_page import BasePage
from ..config.config import Settings_Page,Main_Page_Data,Create_Init_Page

import os
class check_settings_page(BasePage):
    
    def check_settings_add_delete_goal(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Settings_Page.settings_category_btn)
        self.click(Settings_Page.goals_category)
        self.send_keys(Settings_Page.goals_name_field,"TC_5")
        self.click(Settings_Page.goals_plus_btn)
        self.click(Main_Page_Data.home_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.click(Create_Init_Page.pick_a_goal_drop)
        self.find_multiple_elements(Create_Init_Page.pick_a_goal_all_options)
        matched_elements = self.find_multiple_elements(Create_Init_Page.pick_a_goal_all_options)
        a = [i.text for i in matched_elements]
        assert 'TC_5' in a, 'bug'

    
