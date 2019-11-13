from public.pages.management.organ import organPage


class OrganCreditPage(organPage.OrganPage):
    def select_behaviorType(self, behaviorType):
        self.organCredit()
        self.dr.click("xpath->//div[@class='actions']//div[text()='{}']".format(behaviorType))


