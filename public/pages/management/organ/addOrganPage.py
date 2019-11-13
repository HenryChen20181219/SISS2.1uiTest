from public.common.publicfunction import upload_photo
from public.pages.management import registerPage
from public.pages.management.organ import organListPage


class AddOrganPage(registerPage.RegisterPage, organListPage.OrganListPage):

    def input_organCode(self,code):
        self.dr.clear_type("xpath->//input[@name='inputCode']",code)


    # 新增机构
    def addOrgan(self,code, organName, organSimpleName, registerCapital, areaCode, phone, province, city, area, address, busynessScope,
                 email, legalPersonName, legalPersonIdCard, legalPersonPhone, chargePersonName, chargePersonIdCard, chargePersonPhone,
                 address2):
        self.organList()
        self.click_add()
        self.input_organCode(code)
        self.submit()
        self.input_organName(organName)
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
        # 提交
        self.click_submit()


