from public.pages.management import indexPage


class LoginPage(indexPage.IndexPage):
    def input_username(self, username):
        '''输入用户名'''
        self.dr.clear_type('name->username', username)

    def input_password(self, password):
        '''输入密码'''
        self.dr.clear_type('name->password', password)

    def click_agree(self):
        self.dr.click("xpath->//i[@class='layui-icon layui-icon-ok']")

    def click_login(self):
        '''点击提交'''
        self.dr.click('xpath->//button[contains(.,"登录")]')

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()

    # 封装正常登录流程
    def login(self, username, password):
        self.input_username(username)
        self.input_password(password)
        self.click_agree()
        self.click_login()
