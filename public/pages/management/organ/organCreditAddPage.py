import time

from public.common.publicfunction import get_currentTime, upload_photo
from public.pages.management.organ import organCreditPage

date_from, date_to = get_currentTime()


class OrganCreditAddPage(organCreditPage.OrganCreditPage):
    # 输入关键字
    def input_keyWord(self, keyWord):
        self.dr.clear_type("xpath->//input[@placeholder='输入关键字搜索']", keyWord)

    # 选择机构
    def select_organ(self):
        self.dr.click("xpath->(//dd[@ng-repeat='item in list track by $index'])[2]")

    # 点击处理主体
    def click_processSubject(self):
        self.dr.click("xpath->//div[@verify-msg='请选择处理机关'][1]")

    # 选择处理主体
    def select_processSubject(self, processSubject):
        self.dr.click(
            "xpath->//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,'{}')][1]".format(processSubject))

    # 点击行业黑名单类别
    def click_blackListType(self):
        self.dr.click("xpath->//div[@verify-msg='请选择“行业黑名单”类别'][1]")

    # 选择类别
    def select_blackListType(self, blackListType):
        self.dr.click(
            "xpath->//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,'{}')][1]".format(blackListType))

    # 输入行业指标项
    def input_industryIndex(self, industryIndex):
        self.dr.clear_type("xpath->(//input[@placeholder='输入关键字搜索'])[2]", industryIndex)

    # 选择行业指标
    def select_industryIndex(self):
        self.dr.click("xpath->(//div[@verify-msg='请输入行为指标项']//dd)[2]")

    # 点击禁业周期
    def click_period(self):
        self.dr.click("xpath->(//input[@placeholder='yyyy-MM-dd'])[1]")

    # 选择禁业周期
    def select_period(self):
        self.dr.click("xpath->//td[@lay-ymd='{}']".format(date_from))
        script = 'document.querySelector("i.layui-icon.laydate-icon.laydate-next-y").click()'
        self.dr.js(script)
        self.dr.js(script)
        self.dr.click("xpath->//td[@lay-ymd='{}']".format(date_to))

    def confirm_date(self):
        self.dr.click("xpath->//span[@lay-type='confirm']")

    # 输入加入事由
    def input_reason(self, reason):
        self.dr.clear_type("xpath->//textarea[@placeholder='请输入']", reason)

    # 点击确定
    def click_submit(self):
        self.dr.click('xpath->//button[contains(.,"确定")]')

    # 输入统一社会代码
    def input_code(self, code):
        self.dr.clear_type("name->organCode", code)

    # 点击链接确定
    def click_aSubmit(self):
        self.dr.click('xpath->//a[contains(.,"确定")]')

    # 点击不良行为类别
    def click_badBehaviorType(self):
        self.dr.click("xpath->//div[@verify-msg='请选择行为类别'][1]")

    # 选择不良行为类别
    def select_badBehaviorType(self, badBehaviorType):
        self.dr.click(
            "xpath->//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,{})]".format(badBehaviorType))

    # 点击不良行为记录
    def click_badBehaviorList(self):
        self.dr.click("xpath->//div[@verify-msg='请选择行为记录'][1]")

    # 选择不良行为记录
    def select_badBehaviorList(self, badBehaviorList):
        self.dr.click(
            "xpath->//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,{})]".format(badBehaviorList))

    # 点击加入事由附件
    def click_reasonPhoto(self):
        self.dr.click("xpath->//div[@class='layui-upload-drag'][1]")

    # 点击加入事由附件
    def click_notificationPhoto(self):
        self.dr.click("xpath->//div[@class='layui-upload-drag'][2]")

    # 封装记录信息代码
    def recordInfo(self,processSubject,blackListType,industryIndex,reason):
        self.click_processSubject()
        self.select_processSubject(processSubject)
        self.click_blackListType()
        self.select_blackListType(blackListType)
        self.input_industryIndex(industryIndex)
        self.select_industryIndex()
        self.click_period()
        self.select_period()
        self.confirm_date()
        self.input_reason(reason)
        self.click_reasonPhoto()
        upload_photo()
        self.click_notificationPhoto()
        upload_photo()
        self.click_submit()

    # 封装良好不良好行为的操作
    def doBehavior(self,processSubject, badBehaviorType, badBehaviorList, reason):
        self.click_processSubject()
        self.select_processSubject(processSubject)
        self.click_badBehaviorType()
        self.select_badBehaviorType(badBehaviorType)
        self.click_badBehaviorList()
        self.select_badBehaviorList(badBehaviorList)
        self.input_reason(reason)
        self.click_reasonPhoto()
        upload_photo()
        self.click_period()
        self.confirm_date()
        self.click_submit()


    # 封装新增机构黑名单流程
    def addBlackList(self, keyWord, processSubject, blackListType, industryIndex, reason):
        self.select_behaviorType('新增"机构行业黑名单"')
        self.input_keyWord(keyWord)
        time.sleep(2)
        self.select_organ()
        self.recordInfo(processSubject, blackListType, industryIndex, reason)

    # 封装新增机构不良行为记录
    def addBadBehavior(self, code, processSubject, badBehaviorType, badBehaviorList, reason):
        self.select_behaviorType('新增"机构不良行为记录"')
        self.input_code(code)
        self.click_aSubmit()
        self.doBehavior(processSubject, badBehaviorType, badBehaviorList, reason)


    # 封装新增机构良好行为
    def addGoodBehavior(self, code, processSubject, badBehaviorType, badBehaviorList, reason):
        self.select_behaviorType('新增"机构良好行为记录"')
        self.input_code(code)
        self.click_aSubmit()
        self.doBehavior(processSubject, badBehaviorType, badBehaviorList, reason)

    # 封装新增联合协会"机构行业黑名单"
    def addAssociationBlackList(self, keyWord, processSubject, blackListType, industryIndex, reason):
        self.select_behaviorType('新增联合协会"机构行业黑名单"')
        self.input_keyWord(keyWord)
        time.sleep(2)
        self.select_organ()
        self.recordInfo(processSubject,blackListType,industryIndex,reason)

