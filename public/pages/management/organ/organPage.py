from public.pages.management import loginPage
from public.parameters.mps import loginparam


class OrganPage(loginPage.LoginPage):
    def click_organ(self):
        self.dr.move_to_element("xpath->(//span[@ng-show='!isMinSide'][contains(.,'机构')])[1]")
        self.dr.click("xpath->(//span[@ng-show='!isMinSide'][contains(.,'机构')])[1]")

    def click_organList(self):
        self.dr.click("xpath->//span[@ng-show='!isMinSide'][contains(.,'机构列表')]")

    def click_organMember(self):
        self.dr.click("xpath->//span[@ng-show='!isMinSide'][contains(.,'机构会员')]")

    def click_organStar(self):
        self.dr.click("xpath->//span[@ng-show='!isMinSide'][contains(.,'机构星级')]")

    def click_organCredit(self):
        self.dr.click("xpath->//span[@ng-show='!isMinSide'][contains(.,'机构诚信')]")

    def click_organKey(self):
        self.dr.click("xpath->//span[@ng-show='!isMinSide'][contains(.,'机构密钥')]")

    def click_selectType(self):
        self.dr.click("xpath->//div[@list='list']")

    def selectQueryType(self, type):
        self.dr.click("xpath->//span[contains(.,'{}')]".format(type))

    def click_keyWord(self):
        self.dr.click("xpath->//textarea[@placeholder='请输入关键字']")

    def input_keyWord(self, keyWord):
        self.dr.clear_type("xpath->//textarea[@placeholder='请输入关键字']", keyWord)

    def click_query(self):
        self.dr.click("xpath->//button[contains(.,'查询')]")

    def click_clear(self):
        self.dr.click("xpath->//button[contains(.,'清空')]")

    def click_select(self):
        self.dr.click("xpath->//button[contains(.,'高级筛选']")

    def click_content(self):
        self.dr.click("xpath->//tr[@data-index='0']//button[contains(.,'详情')]")

    def click_organName(self):
        self.dr.click("xpath->//tr[@data-index='0']//a[@class='text-link ng-binding']")

    # 进入机构列表
    def organList(self):
        self.login(**loginparam)
        self.click_organ()
        self.click_organList()

    # 进入机构会员列表
    def organMember(self):
        self.login(**loginparam)
        self.click_organ()
        self.click_organMember()

    # 进入机构星级列表
    def organStar(self):
        self.login(**loginparam)
        self.click_organ()
        self.click_organStar()

    # 进入机构诚信列表
    def organCredit(self):
        self.login(**loginparam)
        self.click_organ()
        self.click_organCredit()

    # 通过机构名称查询
    def queryByOrganName(self, organName):
        self.organList()
        self.click_selectType()
        self.selectQueryType("机构名称")
        self.input_keyWord(organName)
        self.click_query()

    # 通过机构统一社会信用代码查询
    def queryByOrganCode(self, organCode):
        self.organList()
        self.click_selectType()
        self.selectQueryType("统一社会信用代码")
        self.input_keyWord(organCode)
        self.click_query()
