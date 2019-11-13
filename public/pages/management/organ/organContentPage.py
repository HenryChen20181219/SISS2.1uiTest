from public.pages.management.organ import organListPage


class OrganContentPage(organListPage.OrganListPage):

    def click_baseInfoChange(self):
        self.dr.click("xpath->//a[contains(.,'机构基本信息变更')]")

    def click_organRecordChange(self):
        self.dr.click("xpath->//a[contains(.,'机构备案资料变更')]")


    def click_organTypeChange(self):
        self.dr.click("xpath->//a[contains(.,'机构行业类别变更')]")

    def click_logout(self):
        self.dr.click("xpath->//a[contains(.,'注销')]")


    def click_baseInfo(self):
        self.dr.click("xpath->//a[contains(.,'基础信息')]")

    def click_member(self):
        self.dr.click("xpath->//a[contains(.,'会员')]")


    def click_star(self):
        self.dr.click("xpath->//a[contains(.,'星级')]")


    def click_credit(self):
        self.dr.click("xpath->//a[contains(.,'诚信')]")


    def click_report(self):
        self.dr.click("xpath->//a[contains(.,'年报')]")


    def click_key(self):
        self.dr.click("xpath->//a[contains(.,'密钥')]")


    # 进入基本信息变更
    def baseInfoChange(self):
        self.organList()
        self.click_content()
        self.click_baseInfoChange()


    # 进入机构备案信息变更
    def organRecordChange(self):
        self.organList()
        self.click_content()
        self.click_organRecordChange()


    # 进入机构行业类别变更
    def organTypeChange(self):
        self.organList()
        self.click_content()
        self.click_organTypeChange()


    # 进入机构注销
    def organLogout(self):
        self.organList()
        self.click_content()
        self.click_logout()






