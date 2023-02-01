from ..pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from time import sleep
from ..config.config import  Create_Init_Page,Main_Page_Data,Ideation_Data

import os
class Check_Create_Init(BasePage):
    
    def check_create_delete(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_1")
        self.send_keys(Create_Init_Page.initiative_description,"test1")
        self.click(Create_Init_Page.pick_a_goal_drop)
        self.click(Create_Init_Page.pick_a_goal_first_option)
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_first_option)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_first_option)
        self.click(Create_Init_Page.create_btn)
        saved_title = self.find_text(Create_Init_Page.TC_1_title_for_checking)
        saved_description = self.find_text(Create_Init_Page.TC_1_description_for_check)
        self.hover(Create_Init_Page.for_hover)
        self.click(Create_Init_Page.delete_dropdown)
        self.click(Create_Init_Page.delete_drop_delete_btn)
        self.click(Create_Init_Page.confirm_btn)
        assert saved_title == 'TC_1','Wrong title or initiative was not created'
        assert saved_description == 'test1','Wrong description'

    def check_create_init_without_title(self):
        self.send_keys(Main_Page_Data.email_field,os.getenv('EMAIL'))
        self.send_keys(Main_Page_Data.pswd_field,os.getenv("PASSWORD"))
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_description,"test2")
        self.click(Create_Init_Page.pick_a_goal_drop)
        self.click(Create_Init_Page.pick_a_goal_first_option)
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_first_option)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_first_option)
        self.click(Create_Init_Page.create_btn)
        validation_error = self.find_text(Create_Init_Page.initiative_title_valid_error)
        assert validation_error == 'Name is required', 'Wrong validation error'
        
    def check_create_init_without_description(self):
        self.send_keys(Main_Page_Data.email_field,"artashes.badalyan.999@gmail.com")
        self.send_keys(Main_Page_Data.pswd_field,"lktinereq")
        self.click(Main_Page_Data.login_btn)
        self.click(Settings_Page.settings_category_btn)
        self.click(Settings_Page.goals_category)
        self.send_keys(Settings_Page.goals_name_field,"TC_5")
        self.click(Settings_Page.goals_plus_btn)
        sleep(2)
        self.click(Main_Page_Data.home_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.click(Create_Init_Page.pick_a_goal_drop)
        matched_goal = self.find_text(Create_Init_Page.pick_a_goal_first_option)
        self.click(Create_Init_Page.initiative_back_btn)
        self.click(Settings_Page.settings_category_btn)
        self.click(Settings_Page.goals_category)
        self.click(Settings_Page.goal_delete_drop)
        self.click(Settings_Page.delete_goal)
        self.click(Main_Page_Data.confirm_btn_popup)
        assert 'TC_5' == matched_goal, 'bug'

    

        
        
