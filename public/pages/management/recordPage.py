from public.common.publicfunction import upload_photo
from public.pages.management import registerPage
from public.parameters.mps import registerParam


class RecordPage(registerPage.RegisterPage):
    def input_personName1(self, personName1):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入姓名'])[1]", personName1)


    def input_personName2(self, personName2):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入姓名'])[2]", personName2)


    def input_personName3(self, personName3):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入姓名'])[3]", personName3)


    def input_personName4(self, personName4):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入姓名'])[4]", personName4)


    def input_personName5(self, personName5):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入姓名'])[5]", personName5)


    def input_personIdCard1(self, personIdCard1):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入证件号码'])[1]", personIdCard1)


    def input_personIdCard2(self, personIdCard2):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入证件号码'])[2]", personIdCard2)


    def input_personIdCard3(self, personIdCard3):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入证件号码'])[3]", personIdCard3)


    def input_personIdCard4(self, personIdCard4):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入证件号码'])[4]", personIdCard4)


    def input_personIdCard5(self, personIdCard5):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入证件号码'])[5]", personIdCard5)


    def input_personPhone1(self, personPhone1):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入手机号码'])[1]", personPhone1)


    def input_personPhone2(self, personPhone2):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入手机号码'])[2]", personPhone2)


    def input_personPhone3(self, personPhone3):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入手机号码'])[3]", personPhone3)


    def input_personPhone4(self, personPhone4):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入手机号码'])[4]", personPhone4)


    def input_personPhone5(self, personPhone5):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入手机号码'])[5]", personPhone5)


    def click_upload1(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[1]")


    def click_upload2(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[2]")


    def click_upload3(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[3]")


    def click_upload4(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[4]")


    def click_upload5(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[5]")


    def click_upload6(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[6]")


    def click_upload7(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[7]")


    def click_upload8(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[8]")


    def click_upload9(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[9]")


    def click_upload10(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[10]")


    def input_transactorName(self, transactorName):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入姓名'])[6]", transactorName)


    def input_transactorIdCard(self, transactorIdCard):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入证件号码'])[6]", transactorIdCard)


    def input_transactorPhone(self, transactorPhone):
        self.dr.clear_type("xpath->(//input[@placeholder='请输入联系电话'])[1]", transactorPhone)


    def input_transactorAddress(self, transactorAddress):
        self.dr.clear_type("xpath->(//textarea[@placeholder='请输入详细地址'])[1]", transactorAddress)

    def click_upload11(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[10]")


    def click_upload12(self):
        self.dr.click("xpath->(//div[contains(@class,'layui-upload-drag')])[11]")


    # 机构备案
    def record(self, personName1, personName2, personName3, personName4, personName5,
               personIdCard1, personIdCard2, personIdCard3, personIdCard4, personIdCard5,
               personPhone1, personPhone2, personPhone3, personPhone4, personPhone5,
               transactorName, transactorIdCard, transactorPhone, transactorAddress):
        self.register(**registerParam)
        self.input_personName1(personName1)
        self.input_personName2(personName2)
        self.input_personName3(personName3)
        self.input_personName4(personName4)
        self.input_personName5(personName5)
        self.input_personIdCard1(personIdCard1)
        self.input_personIdCard2(personIdCard2)
        self.input_personIdCard3(personIdCard3)
        self.input_personIdCard4(personIdCard4)
        self.input_personIdCard5(personIdCard5)
        self.input_personPhone1(personPhone1)
        self.input_personPhone2(personPhone2)
        self.input_personPhone3(personPhone3)
        self.input_personPhone4(personPhone4)
        self.input_personPhone5(personPhone5)
        self.click_upload1()
        upload_photo()
        self.click_upload2()
        upload_photo()
        self.click_upload3()
        upload_photo()
        self.click_upload4()
        upload_photo()
        self.click_upload5()
        upload_photo()
        self.click_upload6()
        upload_photo()
        self.click_upload7()
        upload_photo()
        self.click_upload8()
        upload_photo()
        self.click_upload9()
        upload_photo()
        self.click_upload10()
        upload_photo()
        self.input_transactorName(transactorName)
        self.input_transactorIdCard(transactorIdCard)
        self.input_transactorPhone(transactorPhone)
        self.input_transactorAddress(transactorAddress)
        self.click_upload11()
        upload_photo()
        self.click_upload12()
        upload_photo()
        self.click_submit()



