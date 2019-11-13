from public.pages.person import indexPage


class RegisterPage(indexPage.IndexPage):
    def click_register(self):
        """ 点击注册 """
        self.dr.move_to_element("xpath->//a[@class='cursor-pointer'][contains(.,'注册帐户')]")
        self.dr.click("xpath->//a[@class='cursor-pointer'][contains(.,'注册帐户')]")


    def click_cardType(self):
        """ 点击身份证类型"""
        self.dr.click("xpath->//div[@class='cell-right cell-arrow ng-binding placeholder']")


    def select_cardType1(self):
        """ 选择身份证类型，中华人民共和国居民身份证 """
        self.dr.click("xpath->//a[@class='actionsheet-item ng-binding ng-scope'][contains(.,'中华人民共和国居民身份证')]")


    def select_cardType2(self):
        """ 选择身份证类型，港澳台身份证件 """
        self.dr.click("xpath->//a[@class='actionsheet-item ng-binding ng-scope'][contains(.,'港澳台身份证件')]")


    def select_cardType3(self):
        """ 选择身份证类型，华侨身份证 """
        self.dr.click("xpath->//a[@class='actionsheet-item ng-binding ng-scope'][contains(.,'华侨身份证')]")

    def input_name(self,name):
        """ 输入姓名 """
        self.dr.clear_type("name->name",name)


    def input_idCard(self,idCard):
        """ 输入证件号码 """
        self.dr.clear_type("name->idNo",idCard)


    def click_idCard(self):
        """ 点击身份证类型"""
        self.dr.click("xpath->//img[@src='img/add.png']")

    def submit(self):
        self.dr.click("xpath->//button[@type='button']")


