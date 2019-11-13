from public.pages.person import indexPage


class LoginPage(indexPage.IndexPage):
    def input_idCard(self, idCard):
        '''输入身份证'''
        self.dr.clear_type('name->username',idCard)

    def input_starCard(self, starCard):
        '''有牌人员输入星级服务牌'''
        self.dr.clear_type('name->username',starCard)

    def input_password(self,password):
        '''输入密码'''
        self.dr.clear_type('name->password',password)


    def click_submit(self):
        '''点击提交'''
        self.dr.click('xpath->//a[contains(.,"登录")]')

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()
