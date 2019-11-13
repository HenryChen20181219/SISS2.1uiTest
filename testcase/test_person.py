import unittest

from public.common import mytest
from public.common.publicfunction import upload_photo, get_person_info
from public.pages.person.loginPage import LoginPage
from public.pages.person.registerPage import RegisterPage


name_list, id_card_list = get_person_info(10)


class TestPerson(mytest.MyTest):

    def login(self,username,password):
        '''封装登录'''
        loginPage = LoginPage(self.dr)
        if len(username) == 15:
            loginPage.input_idCard(username)
        else:
            loginPage.input_starCard(username)
        loginPage.input_password(password)
        loginPage.click_submit()
        print(loginPage.return_title())
        self.assertIn("深圳", loginPage.return_title())


    def register(self, name, idCard):
        """ 人员注册封装 """
        registerPage = RegisterPage(self.dr)
        registerPage.click_register()
        registerPage.click_cardType()
        registerPage.select_cardType1() #可以选择3种身份证类型
        registerPage.input_name(name)
        registerPage.input_idCard(idCard)
        upload_photo()
        registerPage.submit()


    @unittest.skip("")
    def test1_loginByIdCard(self):
        """使用数据驱动,进行测试
        身份证登录
        """
        # datas = datainfo.get_xls_to_list('searKey.xlsx', 'Sheet1')
        self.login("513436200011047566","047566")


    @unittest.skip("")
    def test2_loginByStartCart(self):
        """星级服务牌登录"""
        self.login("J2097443","123456")


    def test3_register(self):
        """ 新注册 """
        self.register(name_list[0], id_card_list[0])


    def test4_hasRegistered(self):
        """ 已注册 """
        self.register(name_list[0], id_card_list[0])









