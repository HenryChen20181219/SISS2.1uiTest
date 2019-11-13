from public.common import basepage


class IndexPage(basepage.Page):
    def __init__(self, selenium_driver):
        super().__init__(selenium_driver)
        self.dr.open("http://fenz.ufwl.net")



