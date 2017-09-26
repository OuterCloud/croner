import subprocess
import os
import json

def read_config():
	with open(config_path,"r") as f:
		content = f.read()
		json_ = json.loads(content)
		return json_

root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
config_path = os.path.join(root_path,"config","config")
config = read_config()
git_url = config["git"]
repo_name = git_url.split("/")[len(git_url.split("/"))-1][:-4]
test_scripts_path = os.path.join(root_path,"test","test_scripts")
repo_path = os.path.join(test_scripts_path,repo_name)

def exec_cmd(command):
	ret = subprocess.call(command,shell=True)
	print(ret)

def clone():
	cmd = "git clone "+git_url+" "+repo_path
	if os.path.exists(repo_path):
		os.chdir(repo_path)
		exec_cmd("git pull")
		os.chdir(root_path)
	else:
		exec_cmd(cmd)

	