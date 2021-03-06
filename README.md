# croner
    
    Croner test framework.
    这是一个基于cron和nose开发的简洁python测试框架。

## 0. 介绍
    
### 特点
    
1. 基于本地部署与执行
2. 基于python nose测试框架
3. 基于git管理测试用例
4. 基于cron定时执行测试
    
### 组成

1. 测试脚本仓库

    #在test文件夹的test_scripts文件夹中
    1. 在config文件中配置测试脚本仓库所在的git路径
    2. 执行测试时自动从配置的git路径下载/更新测试用例
    3. 测试用例在git仓库独立维护
    
2. 测试工具

    #在test文件夹的test_tools文件夹中
    1. 提供数据驱动方法
    2. 可以自行添加测试工具文件到该文件夹中
    
3. 定时任务与报警功能

    #在lib文件夹中的cron.py文件中
    1. 利用python cron定时执行测试
    2. 每次执行完测试后对测试结果进行分析
    3. 若有失败的测试结果立刻报警（发邮件/发...）

## 1. 前提
    
1. 已安装python3
2. 已安装python的pip工具
3. 已设置PowerShell脚本执行策略为Unrestricted
4. 已安装python的nose框架并完成了2to3的转换
    
## 2. 配置与安装

1. 配置git安装路径的bin目录路径到path环境变量（例如：C:\Program Files\Git\bin）
2. 执行setup.ps1文件安装requirements.txt文件中指定的python库

## 3. 使用

1. 编写测试用例脚本（示例如下）

```python
# -*- coding: utf-8 -*-
from nose.tools import *
from parameterized import parameterized
import os
import sys
from test.test_tools.test_data_tool import *

@istest
class Test():
    test_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(test_path,"test_data","QueryTradeInfoTester.csv")
    
    @parameterized.expand([
        (file_path, 1),
        (file_path, 2),
        (file_path, 3),
    ])
    def test_1(self, file_path, t_data_number):
        t_data = get_t_data(file_path)
        setattr(self, 't_data', t_data[t_data_number-1])
        print(self.t_data['retCode'])
        assert_equal(self.t_data['retCode'],"200")
```

2. 执行start.ps1文件开始测试

## 4. 帮助

[数据驱动工具的使用方法以及python3下nose的2to3转换](http://www.cnblogs.com/LanTianYou/p/7298200.html)
