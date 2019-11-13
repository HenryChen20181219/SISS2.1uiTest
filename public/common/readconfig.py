import configparser


class ReadConfig():
    def __init__(self,configpath):
        fd = open(configpath)
        data = fd.read()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configpath)

    def getValue(self,env,name):
        '''配置多环境
        [projectConfig]
        project_path=D:/python36/ui_test/SISS2.1
        :param env:[projectConfig]
        :param name:project_path
        :return:D:/python36/ui_test/SISS2.1
        '''
        return self.cf.get(env,name)
