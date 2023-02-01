from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
import time
import random
import string

def randEmail(chars = string.ascii_uppercase + string.digits, N=10):
	return  ''.join(random.choice(chars) + "@gmail.com")

def randPswd(chars = string.ascii_uppercase + string.digits, N=10):
	return  ''.join(random.choice(chars))

class Main_Page_Data():
    new_initiative_btn = (By.XPATH,"//button[@class = 'qp-button initiative-tab-container-button big-btn']")
    new_category_btn = (By.XPATH,"//div[@class = 'initiatives-wrapper--navbar']/div/div/div[3]")
    active_category_btn = (By.XPATH,"//div[@class = 'initiatives-wrapper--navbar']/div/div/div[4]")
    completed_category_btn = (By.XPATH,"//div[@class = 'initiatives-wrapper--navbar']/div/div/div[5]")
    closed_category_btn = (By.XPATH,"//div[@class = 'initiatives-wrapper--navbar']/div/div/div[6]")
    create_new_custom_initiative = (By.XPATH,"//li[@class = 'init-templates-modal--initiatives-block--li init-templates-modal--initiatives-block--li-new-init']")
    email_field = (By.XPATH,"//input[@id = 'EmailAddress']")
    pswd_field = (By.XPATH,"//input[@id = 'Password']")
    login_btn = (By.XPATH,"//button[@type = 'submit']")
    home_btn = (By.XPATH,"//div[@class = 'initiative-bar-container-title' and text() = 'Home']")
    for_tc_4 = (By.XPATH,"//div[text() = 'TC_4']")
    for_tc_6 = (By.XPATH,"//div[text() = 'TC_6']")
    switch_completed_category_btn = (By.XPATH,"//span[text() = 'Completed']")
    switch_closed_category_btn = (By.XPATH,"//span[text() = 'Closed']")
    for_gmail_login = (By.XPATH,"r'https://accounts.google.com/signin/v2/identifier?continue='+\
    'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+\
    '&flowName=GlifWebSignIn&flowEntry = ServiceLogin'")
    body = (By.XPATH,'//body')
    
    

class Create_Init_Page():
    initiative_title = (By.XPATH,"//input[@name = 'name']")
    initiative_description = (By.XPATH,"//textarea[@name = 'description']")
    pick_a_goal_drop = (By.XPATH,"//span[text() = 'Pick a goal']/parent::div")
    pick_a_goal_first_option = (By.XPATH,"//span[text() = 'Pick a goal']/parent::div/following-sibling::div/div[1]")
    pick_a_goal_all_options = (By.XPATH,"//span[text() = 'Pick a goal']/parent::div/following-sibling::div/div")
    select_owner_field = (By.XPATH,"//input[@placeholder = 'Select owner']")
    select_owner_first_option = (By.XPATH,"//div[@class = 'search-dropdown--container search-dropdown--container-open']/div[1]")
    select_contributor = (By.XPATH,"//input[@placeholder = 'Select contributor']")
    select_contributor_first_option = (By.XPATH,"//div[@class = 'search-dropdown--container search-dropdown--container-open']/div[1]")
    create_btn = (By.XPATH,"//button[text() = 'Create']")
    TC_1_title_for_checking = (By.XPATH,"//div[@class = 'lane-page']/div[1]/div/div/div[3]/div[1]")
    TC_1_description_for_check = (By.XPATH,"//div[@class = 'lane-page']/div[1]/div/div/div[3]/div[2]")
    delete_dropdown = (By.XPATH,"//div[@class = 'lane-page']/div[1]//div[@class = 'popover  ']")
    delete_drop_delete_btn = (By.XPATH,"//span[text() = 'Delete']")
    confirm_btn = (By.ID,'confirm-confirm')
    for_hover = (By.XPATH,"//div[@class = 'lane-page']/div[1]")
    initiative_title_valid_error = (By.XPATH,"//input[@name = 'name']/parent::div/label")
    initiative_description_valid_error = (By.XPATH,"//input[@name = 'description']/parent::div/label")

class Inside_Initiative_Page():
    lane_update_drop = (By.XPATH,"//div[@class = 'initiative-info--status']")
    lane_update_active = (By.XPATH,"//span[text() = 'Active']")
    lane_update_completed = (By.XPATH,"//span[text() = 'Completed']")
    lane_update_closed = (By.XPATH,"//span[text() = 'Closed']")
    ideation_category = (By.XPATH,"//span[text() = 'Ideation']")
    new_ideation_btn = (By.XPATH,"//button[@id = 'create-ideation']")

class Settings_Page():
    settings_category_btn = (By.XPATH,"//div[@class = 'initiative-bar-container-title' and text() = 'Settings']")
    goals_category = (By.XPATH,"//span[text() = 'Goals']")
    goals_name_field = (By.XPATH,"//input[@class = 'qp-textInput ']")
    goals_plus_btn = (By.XPATH,"//div[@class = 'goals-page--header-operation']")

class Ideation_Data():
    ideation_title_field = (By.XPATH,"//input[@placeholder='Enter a title for your Ideation']")
    ideation_introduction_field = (By.XPATH,"//textarea[@placeholder = 'Enter a introduction for your Ideation']")
    browser_logo = (By.XPATH,"//div[@class = 'file-uploader']")
    crowdsource_switch = (By.XPATH,"//label[@for = 'Crowdsource request']/div")
    promoted_idea_switch = (By.XPATH,"//label[@for = 'Promoted ideas']/div")
    comments_switch = (By.XPATH,"//label[@for = 'Comments']/div")
    draft_publish_drop = (By.XPATH,"//span[text() = 'Draft']/parent::div")
    publish_option = (By.XPATH,"//div[text() = 'Publish']")
    ideas_1 = (By.XPATH,"//input[@placeholder = 'Idea 1']")
    ideas_2 = (By.XPATH,"//input[@placeholder = 'Idea 2']")
    ideas_3 = (By.XPATH,"//input[@placeholder = 'Idea 3']")
    first_idea_plus_btn = (By.XPATH,"//input[@placeholder = 'Idea 1']/parent::div/button[1]")
    second_idea_btn = (By.XPATH,"//input[@placeholder = 'Idea 2']/parent::div/button[1]")
    see_live_btn = (By.XPATH,"//span[@id = 'see-live']")
    start_page_intro = (By.XPATH,"//p[@class = 'start-page--sub-title']")
    ideation_start_btn = (By.XPATH,"//button[@class = 'qp-button start-page--start-btn']")
    logo_existence = (By.XPATH,"//img")
    add_your_idea_field = (By.XPATH,"//textarea[@placeholder = 'Add your idea here.']")
    submit_btn = (By.XPATH,"//button[@class = 'qp-button idea-page--question--btn']")
    idea1_existence = (By.XPATH,"//div[@class = 'ideas-vote-page--voted-ideas-block']/div[1]/p")
    idea2_existence = (By.XPATH,"//div[@class = 'ideas-vote-page--voted-ideas-block']/div[2]/p")
    idea3_existence = (By.XPATH,"//div[@class = 'ideas-vote-page--voted-ideas-block']/div[3]/p")
    select_first_idea = (By.XPATH,"//div[@class = 'ideas-vote-page--left-block']/div[1]/div[1]")
    select_second_idea = (By.XPATH,"//div[@class = 'ideas-vote-page--left-block']/div[2]/div[1]")
    select_third_idea = (By.XPATH,"//div[@class = 'ideas-vote-page--left-block']/div[3]/div[1]")
    ideation_submit_btn = (By.XPATH,"//button[@class = 'qp-button ']")
    thank_you = (By.XPATH,"//p[@class = 'end-page--sub-sub-title']")
    logo_input = (By.XPATH,"//input[@name = 'file']")
    validation_error_desc = (By.XPATH,"//label[@class = 'error-label']")



    
    
