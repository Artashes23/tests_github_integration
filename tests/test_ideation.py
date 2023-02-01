from ..pages.create_ideation import Check_Ideations


import os



class Test_Ideations(Check_Ideations):
    def test_create_delete_ideations(self,setup):
        self.browser = setup
        self.browser.get('https://empower.questionpro.com/')
        self.check_create_delete()
