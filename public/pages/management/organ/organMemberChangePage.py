from public.pages.management.organ import organMemberPage


class OrganMemberChangePage(organMemberPage.OrganMemberPage):
    def click_submit(self):
        self.dr.click('xpath->//button[contains(.,"提交")]')

    def click_levelOfAfter(self):
        self.dr.click("xpath->//input[@type='text']")

    def select_levelOfAfter(self, level):
        self.dr.click('xpath->//span[contains(.,"{}")]'.format(level))

    # 机构会员类别变更
    def organMemberTypeChange(self):
        self.organMemberTypeChangePage()
        self.click_submit()

    # 机构会员级别变更
    def organMemberLevelChange(self, level):
        self.organMemberLevelChangePage()
        self.click_levelOfAfter()
        self.select_levelOfAfter(level)
        self.click_submit()
