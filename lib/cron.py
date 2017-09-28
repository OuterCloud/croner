# coding:utf-8
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import time,os,sys
import subprocess
from bs4 import BeautifulSoup
import git

croner_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
result_path = os.path.join(croner_path,"test","test_results","result.html")
command = "nosetests --processes="+sys.argv[2]+" --with-html-output --html-out-file="+result_path+" --with-setup-ittr"

#测试用例运行任务
def test_task():
	print('Test start time: %s' % datetime.now())
	retcode = subprocess.call(command,shell=True)
	print('Test end time: %s' % datetime.now())
	fail,result = analyse_result()
	if fail:
		#有未通过的测试用例
		alert(result)

#分析测试结果
def analyse_result():
	soup = BeautifulSoup(open(result_path),"lxml")
	all_p = soup.find_all("p",class_="attribute")
	for p in all_p:
		if "Failure" in p.text:
			return True,p.text
	#用例全部测试通过
	return False,"All pass."

#提醒功能
def alert(result):
	print(result)
	'''
		可以在下面添加发邮件提醒功能
		或通过其他通讯工具发送提醒的功能
	'''

#开始定时器任务
def start_scheduler(seconds):
	scheduler = BlockingScheduler()
	print('Croner is working. Press Ctrl+{0} to exit'.format('c/Enter' if os.name == 'nt' else 'C'))
	test_task()
	scheduler.add_job(test_task,'interval', seconds=int(seconds), id='test_job')
	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		scheduler.shutdown()

if __name__ == '__main__':
	git.clone()
	start_scheduler(sys.argv[1])
