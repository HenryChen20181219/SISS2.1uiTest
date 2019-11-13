from public.pages.management.organ.organPage import OrganPage
from public.parameters.mps import loginparam


class BranchOrganPage(OrganPage):
    def click_branchOrgan(self):
        self.dr.move_to_element("xpath->(//span[@ng-show='!isMinSide'][contains(.,'分支机构')])[1]")
        self.dr.click("xpath->(//span[@ng-show='!isMinSide'][contains(.,'分支机构')])[1]")

    def click_branOrganList(self):
        self.dr.click("xpath->//span[@ng-show='!isMinSide'][contains(.,'分支机构列表')]")

    def click_branchOrganStar(self):
        self.dr.click("xpath->//span[@ng-show='!isMinSide'][contains(.,'分支机构星级')]")

    def click_branchOrganCredit(self):
        self.dr.click("xpath->//span[@ng-show='!isMinSide'][contains(.,'分支机构诚信')]")

    # 进入分支机构列表
    def branchOrganList(self):
        self.login(**loginparam)
        self.click_branchOrgan()
        self.click_organList()

    # 进入分支机构星级列表
    def branchOrganStar(self):
        self.login(**loginparam)
        self.click_branchOrgan()
        self.click_organStar()

    # 进入分支机构诚信列表
    def branchOrganCredit(self):
        self.login(**loginparam)
        self.click_branchOrgan()
        self.click_organCredit()

    # 通过分支机构名称查询
    def queryByBranchOrganName(self, branchOrganName):
        self.branchOrganList()
        self.click_selectType()
        self.selectQueryType("分支机构名称")
        self.input_keyWord(branchOrganName)
        self.click_query()

    # 通过分支机构统一社会信用代码查询
    def queryByBranchOrganCode(self, branchOrganCode):
        self.organList()
        self.click_selectType()
        self.selectQueryType("统一社会信用代码")
        self.input_keyWord(branchOrganCode)
        self.click_query()
        