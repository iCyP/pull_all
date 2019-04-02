import subprocess
import os

cur_dir = os.path.dirname(os.path.abspath(__file__))
git_command = "git pull origin master"
for dir_name in [obj for obj in os.listdir(cur_dir) if os.path.isdir(obj) and obj not in ("__pycache__") and not obj.startswith(".")]:
	cd = f"{os.path.normpath(os.path.join(cur_dir,dir_name))}"
	os.chdir(cd)
	subprocess.run(git_command)