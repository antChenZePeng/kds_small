# -*- coding: utf-8 -*-
##############################################################################
# Copyright (c) wxmall.janedao.cn
# Author：QQ173782910
#QQ group:528289471
##############################################################################
"""config.py"""

import os

DEBUG='1'
ulink=0
md5code = 'janedao'#这是加密的密钥，在安装前可以随便修改，否则导致无法解密，影响使用。
auth_name='ALL'#所有
auth_pass='PASS'#

#这里是调试开关 1是开启，其他值都是关闭,
logconfig=1
# 开启时有问题会向我预设的一个接口发送错误信息，再次申明，不会收集任何个人隐私数据
#################
#这下边是项目路径，预设好的，请不要修改。
CLIENT_NAME = 'Small'
WEBSITE_PATHR = os.path.join('/var/games/', CLIENT_NAME)
fnamer = r'D:/pythonPro/%s/%s.log' %(CLIENT_NAME,CLIENT_NAME)
ROOTR = r'D:/pythonPro'
SITE_ROOTR = r'D:/pythonPro/' + CLIENT_NAME
PDF_OUT_PATHR = r'D:/pythonPro/%s/static/data/pdf'%CLIENT_NAME
ATTACH_ROOTR = r'D:/pythonPro/%s/static/data'%CLIENT_NAME
PEM_ROOTR = r'D:/pythonPro/data_h/%s'%CLIENT_NAME
#################
