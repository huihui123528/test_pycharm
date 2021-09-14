# -*- coding:utf-8 -*-
"""
 作者：会会 zhanghui

 日期：2021年09月13日
 
"""
import os
all_path = []
all_name = []


def check_path(file_path):
    """
    遍历所有子包，并更新文件名
    :param file_path:
    :return:
    """
    # TODO 买票
    for (root, dirs, files) in os.walk(file_path):
        for f in files:
            path = os.path.join(root,f)
            with open('hue_path.txt','a',encoding='gb18030', errors='ignore') as e:
                e.write('\n' + str(path))
                e.close()


file_path = 'C:\\Users\\会会\\Desktop\\fsdownload\\arm'

check_path(file_path)
