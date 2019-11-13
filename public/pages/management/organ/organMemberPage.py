from public.pages.management.organ import organPage


class OrganMemberPage(organPage.OrganPage):
    def click_memberTypeChange(self):
        self.dr.click("//div[contains(.,'会员类别变更']")

    def click_memberLevelChange(self):
        self.dr.click("//div[contains(.,'会员级别变更']")

    # 进入机构会员类别变更页面
    def organMemberTypeChangePage(self):
        self.organMember()
        self.click_content()
        self.click_memberTypeChange()

    # 进入机构会员级别变更页面
    def organMemberLevelChangePage(self):
        self.organMember()
        self.click_content()
        self.click_memberLevelChange()
