import os
import sys
import atexit
import time

class utility():

    def __init__(self):

        pass

    def mkdir(self, path):  ##这个函数创建文件夹

        path = path.strip()

        isExists = os.path.exists(path)

        if not isExists:

            print('创建名字叫做', path, '的文件夹')

            os.makedirs(path)

            print('创建成功！')

        else:

            print(path, '文件夹已经存在了，不再创建')


    def scoll_down(self, driver, times):

        for i in range(times):

            print("开始执行第" + str(i) + "次下拉操作")

            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 执行JavaScript实现网页下拉倒底部

            print("第" + str(i) + "次下拉操作完成")

            print("等待网页加载")

            time.sleep(2)


