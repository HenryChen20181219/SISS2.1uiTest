from public.pages.management.organ import organPage


class OrganListPage(organPage.OrganPage):

    def click_add(self):
        self.dr.click("xpath->//div[@ng-click='add()']")


    def click_hasRecord(self):
        self.dr.click("xpath->//tr[@data-index='0']//button[contains(.,'已备案')]")


    def click_resetPassword(self):
        self.dr.click("xpath->//tr[@data-index='0']//button[contains(.,'重置密码')]")


    def input_newPassword(self,newPassword):
        self.dr.clear_type("name->newPwd",newPassword)


    def submit(self):
        self.dr.click("xpath->//a[@class='layui-layer-btn0'][contains(.,'确定')]")


    # 重置密码
    def resetPassword(self,newPassword):
        self.organList()
        self.click_resetPassword()
        self.input_newPassword(newPassword)
        self.submit()





