import time

from public.common.publicfunction import upload_photo
from public.pages.management.branchOrgan.branchOrganListPage import BranchOrganListPage
from public.pages.management.organ.addOrganPage import AddOrganPage
from public.pages.management.recordPage import RecordPage
from public.parameters.mps import recordParam


class AddBranchOrganPage(AddOrganPage, BranchOrganListPage,RecordPage):
    def input_branchOrganName(self, branchOrganName):
        self.dr.clear_type("xpath->//input[@name='sissOrganBranchVO.name']", branchOrganName)

    def input_address(self, address):
        self.dr.clear_type("xpath->//textarea[contains(@name,'sissOrganBranchVO.address')]", address)

    def input_legalPersonName(self, legalPersonName):
        self.dr.clear_type("xpath->//input[@placeholder='请输入负责人信息姓名']", legalPersonName)

    def input_legalPersonIdCard(self, legalPersonIdCard):
        self.dr.clear_type("xpath->//input[@placeholder='请输入负责人证件号码']", legalPersonIdCard)

    def input_legalPersonPhone(self, legalPersonPhone):
        self.dr.clear_type("xpath->//input[@placeholder='请输入负责人手机号码']", legalPersonPhone)

    # 新增分支机构
    def addBranOrgan(self, code, branchOrganName, phone, province, city, area,
                 address, email, legalPersonName, legalPersonIdCard, legalPersonPhone):
        self.branchOrganList()
        self.click_add()
        self.input_organCode(code)
        self.submit()
        self.input_branchOrganName(branchOrganName)
        # 点击注册日期
        self.click_registerData()
        # 选择注册日期
        self.select_registerData()
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
        # 输入邮箱
        self.input_email(email)
        # 点击营业执照
        self.click_businessLicense()
        # 上传
        upload_photo()
        # 输入法人名字
        self.input_legalPersonName(legalPersonName)
        # 输入法人身份证
        self.input_legalPersonIdCard(legalPersonIdCard)
        # 输入法人手机号
        self.input_legalPersonPhone(legalPersonPhone)
        # 点击同意
        self.click_agree()
        js = "alert('点击地图')"
        self.dr.js(js)
        time.sleep(10)
        # 提交
        self.click_submit()
        #备案
        self.recordOperate(**recordParam)
