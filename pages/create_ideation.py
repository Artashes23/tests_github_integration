from ..pages.base_page import BasePage
from ..config.config import Main_Page_Data,Create_Init_Page,Inside_Initiative_Page,Ideation_Data

import os
from time import sleep
from selenium.webdriver.common.keys import Keys

class Check_Ideations(BasePage):
    
    def check_create_delete(self):
        logo_path = (r"C:\Users\Artashes\Downloads\for_test_.png")
        self.send_keys(Main_Page_Data.email_field,'artashes.badalyan.999+outerloop@gmail.com')
        self.send_keys(Main_Page_Data.pswd_field,'lktinereq')
        self.click(Main_Page_Data.login_btn)
        self.click(Main_Page_Data.new_initiative_btn)
        self.click(Main_Page_Data.create_new_custom_initiative)
        self.send_keys(Create_Init_Page.initiative_title,"TC_6")
        self.send_keys(Create_Init_Page.initiative_description,"test6")
        self.click(Create_Init_Page.pick_a_goal_drop)
        self.click(Create_Init_Page.pick_a_goal_first_option)
        self.click(Create_Init_Page.select_owner_field)
        self.click(Create_Init_Page.select_owner_first_option)
        self.click(Create_Init_Page.select_contributor)
        self.click(Create_Init_Page.select_contributor_first_option)
        self.click(Create_Init_Page.create_btn)
        self.click(Main_Page_Data.for_tc_6)
        self.click(Inside_Initiative_Page.ideation_category)
        self.click(Inside_Initiative_Page.new_ideation_btn)
        sleep(2)
        self.clear(Ideation_Data.ideation_title_field)
        self.clear(Ideation_Data.ideation_introduction_field)
        self.send_keys(Ideation_Data.ideation_title_field,"TC_6")
        self.send_keys(Ideation_Data.ideation_introduction_field,"test6")
        #self.click(Ideation_Data.browser_logo)
        #self.send_keys(Ideation_Data.logo_input,logo_path)
        self.click(Ideation_Data.crowdsource_switch)
        self.click(Ideation_Data.promoted_idea_switch)
        self.send_keys(Ideation_Data.ideas_1,'idea1')
        self.click(Ideation_Data.first_idea_plus_btn)
        self.send_keys(Ideation_Data.ideas_2,'idea2')
        sleep(2)
        self.click(Ideation_Data.second_idea_btn)
        self.clear(Ideation_Data.ideas_3)
        self.send_keys(Ideation_Data.ideas_3,'idea3')
        self.click(Ideation_Data.comments_switch)
        sleep(2)
        self.send_keys(Main_Page_Data.body,Keys.PAGE_UP)
        self.click(Ideation_Data.draft_publish_drop)
        self.click(Ideation_Data.publish_option)
        self.click(Ideation_Data.see_live_btn)
        self.switch_windows(1)
        ideation_inroduction = self.find_text(Ideation_Data.start_page_intro)
        self.click(Ideation_Data.ideation_start_btn)
        sleep(3)
        
        self.send_keys(Ideation_Data.add_your_idea_field,"testidea")
        self.click(Ideation_Data.submit_btn)
        self.click(Ideation_Data.select_first_idea)
        self.click(Ideation_Data.select_second_idea)
        self.click(Ideation_Data.select_third_idea)
        first_idea = self.find_text(Ideation_Data.idea1_existence)
        second_idea = self.find_text(Ideation_Data.idea2_existence)
        third_idea = self.find_text(Ideation_Data.idea3_existence)
        self.click(Ideation_Data.ideation_submit_btn)
        
        success_message = self.find_text(Ideation_Data.thank_you)
        assert ideation_inroduction == 'test6','Wrong ideation title'
        
        assert first_idea == 'idea3',"Wrong first idea"
        assert second_idea == 'idea2',"Wrong second idea"
        assert third_idea == 'idea1',"Wrong third idea"
        
        assert success_message == 'Your votes have been submitted successfully!','Wrong success message'

        
