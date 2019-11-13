from public.common import mytest
from public.pages.management.branchOrgan.addBranchOrganPage import AddBranchOrganPage
from public.pages.management.loginPage import LoginPage
from public.pages.management.organ.addOrganPage import AddOrganPage
from public.pages.management.organ.organCreditAddPage import OrganCreditAddPage
from public.pages.management.organ.organMemberChangePage import OrganMemberChangePage
from public.pages.management.organ.organPage import OrganPage
from public.pages.management.recordPage import RecordPage
from public.pages.management.registerPage import RegisterPage
from public.parameters.mps import registerParam, recordParam, addOrganParam, addBadBehaviorParam, \
    addOrganBlackListParam, addGoodBehaviorParam, addAssociationBlackListParam, addBranchOrganParam


class TestManagement(mytest.MyTest):
    # 使用数据驱动,进行测试，登录测试，用户名密码正确
    # @unittest.skip("不测这个")
    def test11_login(self):
        # datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        loginPage = LoginPage(self.dr)
        loginPage.login("super", "123456")
        if self.dr.element_exist("xpath->//ul/li[1]/a[contains(.,'首页')]"):
            print("通过")
        else:
            print("不通过")

    # 登录测试，用户名正确，密码为空
    def test12_login(self):
        loginPage = LoginPage(self.dr)
        loginPage.login("super", "")
        if self.dr.element_exist("xpath->//ul/li[1]/a[contains(.,'首页')]"):
            print("通过")
        else:
            print("不通过")

    # 测试注册
    # @unittest.skip("不测这个")
    def test2_register(self):
        registerPage = RegisterPage(self.dr)
        registerPage.register(**registerParam)

    # 测试备案
    # @unittest.skip("不测这个")
    def test3_record(self):
        recordPage = RecordPage(self.dr)
        recordPage.record(**recordParam)

    # 测试转到机构列表
    def test4_organList(self):
        organPage = OrganPage(self.dr)
        organPage.organList()

    # 测试转到机构会员列表
    # @unittest.skip("不测这个")
    def test5_organMember(self):
        organPage = OrganPage(self.dr)
        organPage.organMember()

    # 测试转到机构星级列表
    def test6_organStar(self):
        organPage = OrganPage(self.dr)
        organPage.organStar()

    # 测试转到机构诚信列表
    def test7_organCredit(self):
        organPage = OrganPage(self.dr)
        organPage.organCredit()

    # 测试协会新增机构
    def test8_addOrgan(self):
        addOrgan = AddOrganPage(self.dr)
        addOrgan.addOrgan(**addOrganParam)

    # 测试会员机构会员级别变更
    def test9_organMemberTypeChange(self):
        organMemberChangePage = OrganMemberChangePage(self.dr)
        organMemberChangePage.organMemberTypeChange()

    # 测试会员机构会员级别变更
    def test10_organMemberLevelChange(self):
        organMemberChangePage = OrganMemberChangePage(self.dr)
        organMemberChangePage.organMemberLevelChange("")

    # 测试新增机构黑名单
    def test11_addBlackList(self):
        organCreditAddPage = OrganCreditAddPage(self.dr)
        organCreditAddPage.addBlackList(**addOrganBlackListParam)

    # 测试新增机构不良行为记录
    def test12_addBadBehavior(self):
        organCreditAddPage = OrganCreditAddPage(self.dr)
        organCreditAddPage.addBadBehavior(**addBadBehaviorParam)

    # 测试新增机构良好行为记录
    def test13_addGoodBehavior(self):
        organCreditAddPage = OrganCreditAddPage(self.dr)
        organCreditAddPage.addGoodBehavior(**addGoodBehaviorParam)

    # 测试新增机构良好行为记录
    def test14_addAssociationBlackList(self):
        organCreditAddPage = OrganCreditAddPage(self.dr)
        organCreditAddPage.addAssociationBlackList(**addAssociationBlackListParam)

    # 测试机构新增分支机构
    def test15_addBranchOrgan(self):
        adBranchOrganPage = AddBranchOrganPage(self.dr)
        adBranchOrganPage.addBranOrgan(**addBranchOrganParam)