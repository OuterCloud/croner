# croner
Croner test framework.

Croner

	特点
		基于本地部署与执行
		基于python nose测试框架
		基于git管理测试用例
		基于cron定时执行测试
	组成
		测试脚本仓库
			在test文件夹的test_scripts文件夹中
			在config文件中配置测试脚本仓库所在的git路径
			执行测试时自动下载/更新
		测试工具
			在test文件夹的test_tools文件夹中
			提供数据驱动方法
		定时任务
			在lib文件夹中
			利用python cron定时执行测试
		报警功能
			每次执行完测试后对测试结果进行分析
			若有失败的测试结果立刻报警（发邮件/发...）
