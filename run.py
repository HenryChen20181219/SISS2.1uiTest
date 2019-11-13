#coding=utf-8

import unittest
import HTMLTestRunner
import time
from config import globalparam
from public.common import sendmail

def run():
    test_dir = './testcase'
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py') #找到测试用例

    now = time.strftime('%Y-%m-%d_%H_%M_%S')  #打印当前时间
    reportname = globalparam.report_path + '\\' + 'TestResult' + now + '.html'  #保存文件名
    with open(reportname,'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='测试报告',
            description='Test the import testcase'
        )
        runner.run(suite)  #执行
    time.sleep(3)


    # 发送邮件
   # mail = sendmail.SendMail()
  #  mail.send()

if __name__=='__main__':
    run()