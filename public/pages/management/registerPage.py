import time

from public.common.publicfunction import upload_photo
from public.pages.management import indexPage


class RegisterPage(indexPage.IndexPage):
    def click_register(self):
        self.dr.click("xpath->//a[contains(.,'机构用户注册')]")


    def input_code(self,code):
        self.dr.clear_type("name->code",code)


    def click_nextStep(self):
        self.dr.click("xpath->//button[contains(.,'下一步')]")


    def input_organName(self,organName):
        self.dr.clear_type("xpath->//input[contains(@placeholder,'请输入机构名称')]", organName)


    def input_organSimpleName(self,organSimpleName):
        self.dr.clear_type("xpath->//input[contains(@placeholder,'请输入机构简称')]", organSimpleName)



    def click_registerData(self):
        self.dr.click("xpath->//input[@placeholder='yyyy-MM-dd']")


    def select_registerData(self):
        self.dr.click("xpath->//td[@class='layui-this']")


    def input_registerCapital(self, registerCapital):
        self.dr.clear_type("xpath->//input[contains(@placeholder,'请输入注册资本')]", registerCapital)


    def input_areaCode(self, areaCode):
        self.dr.clear_type("xpath->//input[contains(@name,'areaCode')]", areaCode)


    def input_phone(self, phone):
        self.dr.clear_type("xpath->//input[@placeholder='请输入电话号码']", phone)


    def click_province(self):
        self.dr.click("xpath->(//input[@placeholder='请选择省'])[1]")


    def select_province(self, province):
        self.dr.click("xpath->//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,'{}')]".format(province))


    def click_city(self):
        self.dr.click("xpath->(//input[@placeholder='请选择市'])[1]")


    def select_city(self, city):
        self.dr.click("xpath->(//span[contains(.,'{}')])".format(city))


    def click_area(self):
        self.dr.click("xpath->(//input[@placeholder='请选择区'])[1]")


    def select_area(self, area):
        self.dr.click("xpath->(//span[contains(.,'{}')])".format(area))


    def input_address(self, address):
        self.dr.clear_type("xpath->//textarea[contains(@name,'officeAddress')]", address)


    def input_busynessScope(self, busynessScope):
        self.dr.clear_type("xpath->//textarea[@placeholder='请输入经营范围']", busynessScope)


    def click_companyType(self):
        self.dr.click("xpath->//input[@placeholder='--请选择--']")


    def select_companyType(self):
        self.dr.click("xpath->(//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,'有限责任公司')])[1]")


    def input_email(self, email):
        self.dr.clear_type("xpath->//input[@placeholder='请输入保密邮箱']", email)


    def click_businessLicense(self):
        self.dr.click("xpath->(//div[@class='layui-upload-drag'][contains(.,'点击上传，或将文件拖拽到此处')])[1]")


    def click_Logo(self):
        self.dr.click("xpath->(//div[@class='layui-upload-drag'][contains(.,'点击上传，或将文件拖拽到此处')])[2]")


    def input_legalPersonName(self, legalPersonName):
        self.dr.clear_type("xpath->//input[@placeholder='请输入法定代表人姓名']", legalPersonName)


    def input_legalPersonIdCard(self, legalPersonIdCard):
        self.dr.clear_type("xpath->//input[@placeholder='请输入法定代表人证件号码']", legalPersonIdCard)


    def input_legalPersonPhone(self, legalPersonPhone):
        self.dr.clear_type("xpath->//input[@placeholder='请输入法定代表人手机号码']", legalPersonPhone)


    def click_busynessInfo(self):
        self.dr.click("xpath->(//i[contains(@class,'layui-icon layui-icon-ok')])[1]")


    def input_chargePersonName(self, chargePersonName):
        self.dr.clear_type("xpath->//input[@placeholder='请输入经办人姓名']", chargePersonName)


    def input_chargePersonIdCard(self, chargePersonIdCard):
        self.dr.clear_type("xpath->//input[@placeholder='请输入经办人身份证号码']", chargePersonIdCard)


    def input_chargePersonPhone(self, chargePersonPhone):
        self.dr.clear_type("xpath->//input[@placeholder='请输入经办人手机号码']", chargePersonPhone)


    def get_verifyCode(self):
        self.dr.click("xpath->//button[@class='layui-btn layui-btn-default ng-binding'][contains(.,'获取验证码')]")


    def input_verifyCode(self,verifyCode):
        '''
        输入验证码
        :param verifyCode:从redis获取
        :return:
        '''
        self.dr.clear_type("xpath->//input[@placeholder='请输入验证码']", verifyCode)


    def click_province2(self):
        self.dr.click("xpath->(//input[@placeholder='请选择省'])[2]")


    def select_province2(self, province):
        self.dr.click("xpath->(//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,'{}')])[2]".format(province))


    def click_city2(self):
        self.dr.click("xpath->(//input[@placeholder='请选择市'])[2]")

    def select_city2(self, city):
        self.dr.click(
            "xpath->(//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,'{}')])[2]".format(city))


    def click_area2(self):
        self.dr.click("xpath->(//input[@placeholder='请选择区'])[2]")

    def select_area2(self, area):
        self.dr.click(
            "xpath->(//span[@class='text-ellipsis ng-binding ng-scope'][contains(.,'{}')])[2]".format(area))


    def input_address2(self, address2):
        self.dr.clear_type("xpath->//textarea[@name='contact.address']", address2)


    def click_agree(self):
        self.dr.click("xpath->//span[contains(.,'我同意')]/following-sibling::i")


    def click_submit(self):
        self.dr.click("css->button.ng-isolate-scope")


    # 机构注册
    def register(self, code, organName, organSimpleName, registerCapital, areaCode, phone, province, city, area, address, busynessScope,
                 email, legalPersonName, legalPersonIdCard, legalPersonPhone, chargePersonName, chargePersonIdCard, chargePersonPhone,
                 address2):
        # 点击注册
        self.click_register()
        # 输入统一社会信用代码
        self.input_code(code)
        # 点击下一步
        self.click_nextStep()
        # 输入机构名称
        self.input_organName(organName)
        # 输入机构简称
        self.input_organSimpleName(organSimpleName)
        # 点击注册日期
        self.click_registerData()
        # 选择注册日期
        self.select_registerData()
        # 输入注册资本
        self.input_registerCapital(registerCapital)
        # 输入地区编码
        self.input_areaCode(areaCode)
        # 输入手机号码
        self.input_phone(phone)
        # 点击省份
        self.click_province()
        # 选择省份
        self.select_province(province)
        # 点击市
        self.click_city()
        # 选择市
        self.select_city(city)
        # 点击区
        self.click_area()
        # 选择区
        self.select_area(area)
        # 输入详细地址
        self.input_address(address)
        # 输入业务范围
        self.input_busynessScope(busynessScope)
        # 点击注册类型
        self.click_companyType()
        # 选择注册类型
        self.select_companyType()
        # 输入邮箱
        self.input_email(email)
        # 点击营业执照
        self.click_businessLicense()
        # 上传
        upload_photo()
        # 点击Logo
        self.click_Logo()
        # 上传
        upload_photo()
        # 输入法人名字
        self.input_legalPersonName(legalPersonName)
        # 输入法人身份证
        self.input_legalPersonIdCard(legalPersonIdCard)
        # 输入法人手机号
        self.input_legalPersonPhone(legalPersonPhone)
        # 点击业务信息
        self.click_busynessInfo()
        # 输入经办人姓名
        self.input_chargePersonName(chargePersonName)
        # 输入经办人身份证
        self.input_chargePersonIdCard(chargePersonIdCard)
        # 输入经办人手机号
        self.input_chargePersonPhone(chargePersonPhone)
        # 获取验证码
        self.get_verifyCode()
        # 输入验证码
        # self.input_verifyCode(verifyCode=)
        time.sleep(30)
        # 点击省份2
        self.click_province2()
        # 选择省份2
        self.select_province2(province)
        # 点击市2
        self.click_city2()
        # 选择市2
        self.select_city2(city)
        # 点击区2
        self.click_area2()
        # 选择区2
        self.select_area2(area)
        # 详细地址
        self.input_address2(address2)
        # 点击同意
        self.click_agree()
        # 提交
        self.click_submit()
