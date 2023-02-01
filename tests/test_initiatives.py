from ..pages.create_delete_initiative import Check_Create_Init
import os
import pytest



class Test_Create_Delete_Init(Check_Create_Init):

   

    
    def test_create_delete_init(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('Prod_Url'))
        self.check_create_delete()

    def test_create_init_without_title(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('Prod_Url'))
        self.check_create_init_without_title()

    def test_create_init_without_description(self,setup):
        self.browser = setup
        self.browser.get(os.getenv('PROD_URL'))
        self.check_create_init_without_description()

    

    
        
    
    
    

    

    
    

